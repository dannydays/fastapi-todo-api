import models
from fastapi import HTTPException, status
from hash import Hash


def get_users(db, current_user):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not admin"
        )
    return db.query(models.User).all()

def get_user_by_id(db, id, current_user):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not admin")

    db_user = db.query(models.User).filter(models.User.id == id).first()
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    return db_user

def create_user(db, user):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado."
        )
    
    db_user = models.User(
        name=user.name, 
        email=user.email, 
        password=Hash.bcrypt(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {'detail': 'User created!'}

def update_user(db, user_update, current_user):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    curr_email = current_user.email
    
    db_user = db.query(models.User).filter(models.User.email == curr_email).first()
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    if user_update.name:
        db_user.name = user_update.name
    
    if user_update.email:
        db_user_email_check = db.query(models.User).filter(models.User.email == user_update.email).first()
        if db_user_email_check:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado"
            )
        db_user.email = user_update.email
    
    if user_update.password:
        db_user.password = Hash.bcrypt(user_update.password)
    
    db.commit()
    db.refresh(db_user)
    
    return {"detail": "Dados atualizados com sucesso"}

def delete_user_by_id(user_id: int, db, current_user):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    if current_user.email != db_user.email and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ação não autorizada"
        )

    db.delete(db_user)
    db.commit()    
    return {"detail": "Usuário excluído com sucesso"}
