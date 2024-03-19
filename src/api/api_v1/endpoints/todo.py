from fastapi import APIRouter, Depends, status
from schemas import TodoRequest, TodoResponse, TodoCreate
from api.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from db.models import User
import crud

router = APIRouter()


@router.post("/")
def create_todo(
    todo: TodoRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = crud.todos.create(
        db, obj_in=todo, user_id=current_user.id
    )
    todo_schema = TodoCreate(
        title=todo.title, description=todo.description,
        category_id=todo.category_id
        )
    return TodoResponse(
        message="Success",
        status=str(status.HTTP_201_CREATED),
        todo=todo_schema
        
    )