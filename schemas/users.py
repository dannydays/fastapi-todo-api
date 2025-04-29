from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, List
from schemas.tasks import Task



class BaseUser(BaseModel):
    name: str
    email: EmailStr

class UserCreate(BaseUser):
    password: Annotated[str, Field(min_length=8)]

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)

    model_config = {
        "from_attributes": True
    }

class ShowUser(BaseUser):
    tasks: List[Task]