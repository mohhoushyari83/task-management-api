from fastapi import APIRouter, HTTPException
from app.models import Task

router = APIRouter()

tasks = []
next_id = 1


@router.get("/tasks")
def get_tasks():
    return tasks


@router.post("/tasks")
def create_task(task: Task):
    global next_id

    new_task = {
        "id": next_id,
        **task.model_dump()
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task.model_dump())
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
