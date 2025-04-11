from ai_config import *

if __name__ == "__main__":
    """只是用于测试的简单服务器，很简单，仅供参考，很多异常处理没有写，生产环境请不要使用"""

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=12309)
