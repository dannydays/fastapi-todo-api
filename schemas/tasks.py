from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, List




class Task(BaseModel):
    id: int
    name: str
    check: bool

class TaskCreate(BaseModel):
    name: str
    model_config = {
        "from_attributes": True
    }

class TaskUpdate(TaskCreate):
    pass