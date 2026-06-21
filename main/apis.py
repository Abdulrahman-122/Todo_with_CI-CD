from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from main.database import get_db
from main.models import Todo, User
from main.schemas import TodoCreate, TodoUpdate, TodoResponse
from main.dependency import get_current_user

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse, status_code=201)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_todo = Todo(title=todo.title, completed=todo.completed, user_id=current_user.id)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@router.get("/", response_model=list[TodoResponse])
def get_todos(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return db.query(Todo).filter(Todo.user_id == current_user.id).all()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    payload: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    if payload.title is not None:
        todo.title = payload.title

    if payload.completed is not None:
        todo.completed = payload.completed

    db.commit()
    db.refresh(todo)

    return todo


@router.delete("/{todo_id}", status_code=204)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
