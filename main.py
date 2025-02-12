from fastapi import FastAPI, Request
from persistence import tasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    id: int
    name: str | None = None

@app.get("/api/get")
async def get():
    data = await tasks.get_all()
    return data

@app.post("/api/create")
async def create(task: Task):
    result = await tasks.insert(task.name)
    if result is not None:
        return result
    return {"Successful": "New task created"}


@app.post("/api/remove/{id}")
async def remove(id: int):
    result = await tasks.remove(id)
    if result is not None:
        return result
    return {"Successful": "Task was deleted"}