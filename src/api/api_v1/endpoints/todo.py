from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud
from api.deps import get_current_user, get_db
from db.models import User
from schemas import TodoCreate, TodoRequest, TodoResponse

router = APIRouter()


@router.get("/")
def get_todos(
    per_page: int,
    page: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todos = crud.todos.get_all_by_user_id(db, user_id=current_user.id)
    return TodoResponse(
        message="Success",
        status=str(status.HTTP_200_OK),
        data=[
            TodoCreate(
                title=t.title, description=t.description, category_id=t.category_id
            )
            for t in todos
        ],
    )


@router.post("/")
def create_todo(
    todo: TodoRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = crud.todos.create(db, obj_in=todo)
    todo_schema = TodoCreate(
        title=todo.title, description=todo.description, category_id=todo.category_id
    )
    return TodoResponse(
        message="Success", status=str(status.HTTP_201_CREATED), data=[todo_schema]
    )


@router.put("/{todo_id}")
def update_todo(
    todo_id: str, todo: TodoRequest, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = crud.todos.update_by_todo_id(
        db, obj_in= todo, todo_id=todo_id
    )
    if todo is not None:
        todo_schema = TodoCreate(
            title=todo.title, description=todo.description, category_id=todo.category_id
        )
        return TodoResponse(
            message="Success",
            status=str(status.HTTP_200_OK),
            data=[todo_schema],
        )
    else:
        return TodoResponse(
            message="Todo not found",
            status=str(status.HTTP_404_NOT_FOUND),
            data=[],
        )
    

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = crud.todos.delete_by_todo_id(
        db, todo_id=todo_id
    )
    if todo is not None:
        return TodoResponse(
            message="Success",
            status=str(status.HTTP_200_OK),
            data=[],
        )
    else:
        return TodoResponse(
            message="Todo not found",
            status=str(status.HTTP_404_NOT_FOUND),
            data=[],
        )