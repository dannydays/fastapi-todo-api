import models
from fastapi import HTTPException, status



def get_tasks(db, email):
    tasks = db.query(models.Task).join(models.User).filter(models.User.email == email).all()
    return tasks

def create_task(db, task, email):
    user = db.query(models.User).filter(models.User.email == email).first()

    db_task = models.Task(
        name=task.name,
        check=False,
        user_id=user.id
    )

    if db.query(models.Task).filter(models.Task.name == task.name).first():
        raise HTTPException(
            status_code=409,
            detail="Task name already exists")
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    return {'detail': 'Task created!'}

def check_task(task_id, db, email):
    db_task = db.query(models.Task).filter(models.Task.creator.has(email=email)).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found")
    
    db_task.check = not db_task.check
    db.commit()
    db.refresh(db_task)
    return {'detail': 'task checked', 'current value': db_task.check}

def update_task(task_id, task, db, email):
    db_task = db.query(models.Task).filter(models.Task.creator.has(email=email)).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found")
    
    if task.name:
        db_task.name = task.name
    
    db.commit()
    db.refresh(db_task)
    
    return {'detail': 'Task updated!'}

def delete_task(task_id, db, email):
    db_task = db.query(models.Task).filter(models.Task.creator.has(email=email)).filter(models.Task.id == task_id)
    if not db_task.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found")

    db_task.delete(synchronize_session=False)
    db.commit()

    return {'detail': 'Task deleted!'}

def delete_all_tasks(db, email):
    db_tasks = db.query(models.Task).filter(models.Task.creator.has(email=email)).all()
    if not db_tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No tasks found")

    for task in db_tasks:
        db.delete(task)
    
    db.commit()

    return {'detail': 'All tasks deleted!'}