from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from schemas.users import ShowUser, BaseUser, UserCreate, UserUpdate
from schemas.token import TokenData
from crud import users
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def get_users(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return users.get_users(db, current_user)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return users.get_user_by_id(db, id, current_user)

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return users.create_user(db, user)

@router.put('/', status_code=status.HTTP_200_OK)
def update_user(user_update: UserUpdate, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return users.update_user(db, user_update, current_user)

@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return users.delete_user_by_id(user_id, db, current_user)
