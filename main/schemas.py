from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1)
    completed: bool = Field(default=False)


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str = Field(None, min_length=1)
    completed: bool = None


class TodoResponse(TodoBase):
    id: int

    class Config:
        from_attributes = True
        # tells fastapi to be able to read data from models of database.


class UserCreate(BaseModel):

    username: str = Field(..., min_length=3, example="your username")
    email: str = Field(..., example="name@demo.com")
    password: str = Field(..., min_length=3, example="securepass123")


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
