from typing import Optional

from sqlalchemy.orm import Session

from db.models import Category
from schemas import CategoryCreate, CategoryUpdate

from .base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create(
        self, db: Session, obj_in: CategoryCreate, user_id: int
    ) -> Optional[Category]:
        db_obj = Category(obj_in.model_dump(), user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, user_id: int) -> Optional[Category]:
        categories = db.query(Category).filter(Category.user_id == user_id).all()
        return categories


category = CRUDCategory(Category)
