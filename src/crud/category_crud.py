from typing import Optional

from sqlalchemy.orm import Session

from db.models import Category
from schemas import CategoryCreate, CategoryUpdate

from .base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create(
        self, db: Session, obj_in: CategoryCreate, user_id: int
    ) -> Optional[Category]:
        db_obj = Category(name=obj_in.name, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_by_user_id(self, db: Session, user_id: int, page: int, per_page: int) -> Optional[Category]:
        limit = per_page
        page = page
        offset = (limit * page) - limit
        categories = db.query(Category).filter(Category.user_id == user_id).limit(limit).offset(offset).all()
        return categories
    
    def count_data_by_user_id(self, db: Session, user_id: int):
        return db.query(Category).filter(Category.user_id == user_id).count()

    def update(
        self, db: Session, obj_in: CategoryCreate, user_id: int
    ) -> Optional[Category]:
        category = (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .filter(Category.id == obj_in.id)
            .first()
        )
        if category is not None:
            category.name = obj_in.name
            category.user_id = user_id
            db.add(category)
            db.commit()
            db.refresh(category)
            return category
        else:
            return None

    def delete(self, db: Session, *, id: int, user_id: int) -> Optional[Category]:
        category = (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .filter(Category.id == id)
            .first()
        )
        if category is not None:
            db.delete(category)
            db.commit()
            return category
        else:
            return None


category = CRUDCategory(Category)
