from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from schemas.users import BaseUser
from schemas.tasks import Task, TaskCreate
from schemas.token import TokenData
from crud import tasks
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router.get('/',response_model=List[Task])
def get_tasks(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.get_tasks(db, current_user.email)

@router.post('/')
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.create_task(db, task, current_user.email)

@router.put('/check/{task_id}')
def check_task(task_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.check_task(task_id, db, current_user.email)

@router.put('/{task_id}')
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.update_task(task_id, task, db, current_user.email)

@router.delete('/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.delete_task(task_id, db, current_user.email)

@router.delete('/')
def delete_all_tasks(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return tasks.delete_all_tasks(db, current_user.email)