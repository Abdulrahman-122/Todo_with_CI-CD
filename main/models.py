from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from main.database import Base
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    todos = relationship("Todo", backref="owner")
    is_active = Column(Boolean, default=True)
