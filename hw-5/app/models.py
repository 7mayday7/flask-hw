from pydantic import BaseModel

# Модель для задачи
class Task(BaseModel):
    title: str
    description: str
    status: str = "not completed"
