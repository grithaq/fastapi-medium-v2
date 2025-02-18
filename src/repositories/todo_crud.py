from typing import Optional

from sqlalchemy.orm import Session

from db.models import User, Category, Todo
from schemas import TodoCreate, TodoUpdate

from .base import CRUDBase


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def get_all_by_user_id(self, db: Session, user_id: int, per_page: int, page: int) -> Optional[Todo]:
        limit = per_page
        page = page
        offset = (limit * page) - limit
        todo = db.query(
            User.id.label("user_id"), User.email,
            Category.id.label("category_id"), Category.name.label("category_name"),
            Todo.id.label("todo_id"), Todo.title, Todo.description
            ).join(Category, Category.user_id == User.id).join(Todo, Todo.category_id == Category.id).filter(User.id == user_id).limit(limit).offset(offset).all()
        return todo
    
    def count_data_by_user_id(self, db: Session, user_id: int) -> int:
        return db.query(User, Category, Todo).join(
            Category, Category.user_id == User.id
        ).join(
            Todo, Todo.category_id == Category.id
        ).filter(User.id == user_id).count()

    def create(
        self, db: Session, *, obj_in: TodoCreate
    ) -> Optional[Todo]:
        db_obj = Todo(
            title=obj_in.title, description=obj_in.description,
            category_id=obj_in.category_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_by_todo_id(
        self,
        db: Session,
        todo_id: int,
        obj_in: TodoUpdate
    ):
        todo_from_db = db.query(Todo).filter(Todo.id == todo_id).first()
        if todo_from_db is not None:
            todo_from_db.title = obj_in.title
            todo_from_db.description = obj_in.description
            todo_from_db.category_id = obj_in.category_id
            db.add(todo_from_db)
            db.commit()
            db.refresh(todo_from_db)
            return todo_from_db
        else:
            return None
    
    def delete_by_todo_id(
        self,
        db: Session,
        todo_id: int
    ):
        todo_from_db = db.query(Todo).filter(Todo.id == todo_id).first()
        if todo_from_db is not None:
            db.delete(todo_from_db)
            db.commit()
            return "success"
        else:
            return None
        

todos = CRUDTodo(Todo)
