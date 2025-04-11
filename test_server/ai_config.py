from typing import List

from pydantic import BaseModel
from fastapi_app import app

from log_decorators import performance_logger


class AIConfig(BaseModel):
    id: int
    name: str
    params: int


ai_config_list: List[AIConfig] = []

for i in range(1):
    ai_config_list.append(AIConfig(id=i, name=f"AI-{i}", params=i * 2))


@app.get("/ai_list")
@performance_logger
async def ai_list_api():
    return {"code": 200, "data": ai_config_list, "message": "success"}


@app.get("/ai_detail/{ai_id}")
@performance_logger
async def ai_detail_api(ai_id: int):
    ai_detail = ai_config_list[int(ai_id)]
    return {"code": 200, "data": ai_detail, "message": "success"}


@app.post("/ai_create")
@performance_logger
async def ai_create_api(ai_config: AIConfig):
    ai_config.id = len(ai_config_list)
    ai_config_list.append(ai_config)
    return {"code": 200, "data": ai_config, "message": "success"}


@app.put("/ai_upload/{ai_id}")
@performance_logger
async def ai_update_api(ai_id: int, ai_config: AIConfig):
    ai_config_list[int(ai_id)] = ai_config
    return {"code": 200, "data": ai_config_list[int(ai_id)], "message": "success"}


@app.delete("/ai_delete/{ai_id}")
@performance_logger
async def ai_delete_api(ai_id: int):
    ai_config_list.pop(int(ai_id))
    return {"code": 200, "data": {}, "message": "success"}
