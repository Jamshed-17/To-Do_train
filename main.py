from fastapi import FastAPI, Request
from persistence import tasks
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    name: str | None = None

@app.get("/get")
async def get():
    data = await tasks.get_all()
    return data

@app.post("/create")
async def create(task: Task):
    result = await tasks.insert(task.id, task.name)
    if result is not None:
        return result
    return {"Successful": "New task created"}


@app.post("/remove/{id}")
async def remove(id: int):
    result = await tasks.remove(id)
    if result is not None:
        return result
    return {"Successful": "Task was deleted"}