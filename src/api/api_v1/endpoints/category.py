from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_current_user, get_db
from db.models import User
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
    category = CategoryRequest(id=category.id, name=category.name)
    category_response = CategoryResponse(
        status="201", message="Success", categories=[category]
    )
    return category_response
