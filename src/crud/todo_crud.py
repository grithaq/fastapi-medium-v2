from typing import Optional

from sqlalchemy.orm import Session

from db.models import Todo
from schemas import TodoCreate, TodoUpdate

from .base import CRUDBase


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def create(self, db: Session, *, obj_in: TodoCreate, user_id: int) -> Optional[Todo]:
        db_obj = Todo(**obj_in.dict(), user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


todos = CRUDTodo(Todo)
