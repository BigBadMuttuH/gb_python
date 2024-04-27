from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import TypedDict, Optional
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Task(TypedDict):
    id: int
    title: str
    description: Optional[str]
    status: Optional[str]


tasks_list: list[Task] = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "status": "in progress"},
    {"id": 2, "title": "Task 2", "description": "Description 2", "status": "in progress"},
    {"id": 3, "title": "Task 3", "description": "Description 3", "status": "in progress"},
]


@app.get("/tasks")
async def read_tasks():
    return tasks_list


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for t in tasks_list:
        if t["id"] == task_id:
            t["title"] = task["title"]
            t["description"] = task["description"]
            t["status"] = task["status"]
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for t in tasks_list:
        if t["id"] == task_id:
            tasks_list.remove(t)
            return t
    raise HTTPException(status_code=404, detail="Task not found")
