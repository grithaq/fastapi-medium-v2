from typing import Optional
from .base import CRUDBase
from db.models import Category
from schemas import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create(self, db: Session, obj_in: CategoryCreate) -> Optional[Category]:
        db_obj = Category(
            id=obj_in.id,
            name=obj_in.name
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_categories(self, db: Session):
        categories = db.query(Category).all()
        return categories
    

category = CRUDCategory(Category)