from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class TaskBase(BaseModel):
    title: str
    description: str
    status: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int


tasks_db = []
task_id_counter = 1


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks_db if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    task_id_counter += 1
    tasks_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    task = next((task for task in tasks_db if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    return task


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = next((task for task in tasks_db if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db.remove(task)
    return task
