from fastapi import FastAPI
from database import Base, engine
from routers import users, tasks, authentication

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(tasks.router)
app.include_router(users.router)
