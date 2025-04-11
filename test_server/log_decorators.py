import time
from functools import wraps
import traceback


def safe_log(data, sensitive_keys=["password"]):
    """
    对敏感信息进行脱敏的实现。

    :param data: 需要进行日志记录的数据，可以是字典、列表或其他数据类型。
    :param sensitive_keys: 敏感信息的关键词列表。
    :return: 脱敏后的数据。
    """
    # 判断输入类型，以决定如何处理
    if isinstance(data, dict):
        # 对字典进行递归处理
        return {
            k: safe_log(v, sensitive_keys)
            if isinstance(v, (dict, list))
            else ("REDACTED" if k in sensitive_keys else v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        # 对列表进行遍历和递归处理
        return [safe_log(item, sensitive_keys) for item in data]
    return data  # 对于其他类型的数据，直接返回


def performance_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"=============  Begin: {func.__name__}  =============")
        print(f"参数: ===> {safe_log(kwargs)}")
        try:
            rsp = await func(*args, **kwargs)  # 确保使用 await
            print(f"响应: <=== {safe_log(rsp)}")
            end = time.perf_counter()
            print(f"耗时: {end - start:.3f}s")
            print(f"=============   End: {func.__name__}   =============")
            return rsp
        except Exception as e:
            print(traceback.format_exc())
            print(f"异常: {e}")
            raise e

    return wrapper
