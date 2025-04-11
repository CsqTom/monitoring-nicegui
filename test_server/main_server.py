from fastapi import FastAPI

app = FastAPI()


@app.get("/ai_list")
async def ai_list_api():
    ai_list = []
    for i in range(10):
        ai_list.append({"id": i, "name": f"AI{i}", "params": i * 2})

    return {"code": 200, "data": ai_list, "message": "success"}


@app.get("/ai_detail/{ai_id}")
async def ai_detail_api(ai_id: int):
    ai_detail = {"id": ai_id, "name": f"AI{ai_id}", "params": ai_id * 2}
    return {"code": 200, "data": ai_detail, "message": "success"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=12309)
