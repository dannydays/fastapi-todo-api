from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    name = Column(
        String,
        nullable=False
    )
    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )
    password = Column(
        String,
        nullable=False
    )

    tasks = relationship(
        "Task",
        back_populates="creator"
    )
    is_admin = Column(
        Boolean,
        default=False
    )

class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
        )
    name = Column(
        String,
        unique=True,
        nullable=False
        )
    check = Column(
        Boolean,
        default=False
        )
    user_id = Column(
        Integer, ForeignKey('users.id')
    )
    creator = relationship(
        "User", back_populates="tasks"
    )