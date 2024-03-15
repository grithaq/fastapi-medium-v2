from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.deps import get_current_user, get_db
from db.models import User
import crud
from src.schemas.category import CategoryRequest, CategoryResponse

router = APIRouter()


@router.post(
    "/",
)
def create_category(
    category: CategoryRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category_obj = crud.category.create(db, obj_in=category)
    category_schema = CategoryRequest(id=category_obj.id, name=category_obj.name)
    return CategoryResponse(
        categories=[category_schema],
        message="Success",
        status=str(status.HTTP_201_CREATED)
    )
    
