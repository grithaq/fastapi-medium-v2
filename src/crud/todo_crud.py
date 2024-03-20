from typing import Optional

from sqlalchemy.orm import Session

from db.models import Todo
from schemas import TodoCreate, TodoUpdate

from .base import CRUDBase


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def get_all_by_user_id(self, db: Session, user_id: int) -> Optional[Todo]:
        todos = db.query(Todo).filter(Todo.user_id == user_id).all()
        return todos

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


todos = CRUDTodo(Todo)
