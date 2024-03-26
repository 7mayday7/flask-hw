from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель для задачи
class Task(BaseModel):
    title: str
    description: str
    status: str = "not completed"

# Хранилище задач
tasks_db = []

# Конечная точка для получения списка всех задач
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

# Конечная точка для получения задачи по идентификатору
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < len(tasks_db):
        return tasks_db[task_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

# Конечная точка для добавления новой задачи
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Конечная точка для обновления задачи по идентификатору
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < len(tasks_db):
        tasks_db[task_id] = task
        return task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

# Конечная точка для удаления задачи по идентификатору
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks_db):
        deleted_task = tasks_db.pop(task_id)
        return {"detail": "Task deleted successfully", "deleted_task": deleted_task}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
