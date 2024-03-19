from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud
from api.deps import get_current_user, get_db
from db.models import User
from src.schemas.category import CategoryRequest, CategoryResponse, CategorySchema

router = APIRouter()


@router.get("/")
def get_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    print(current_user.id)
    categories = crud.category.get(db, user_id=current_user.id)
    categories = [CategorySchema(user_id=category.user_id,id=category.id, name=category.name) for category in categories]
    return CategoryResponse(
        message="Success",
        status=str(status.HTTP_200_OK),
        categories=categories
    )


@router.post(
    "/",
)
def create_category(
    category: CategoryRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category_obj = crud.category.create(db, obj_in=category, user_id=current_user.id)
    category_schema = CategoryRequest(id=category_obj.id, name=category_obj.name)
    return CategoryResponse(
        categories=[category_schema],
        message="Success",
        status=str(status.HTTP_201_CREATED),
    )


@router.put("/{category_id}")
def update_category(
    category_id: str,
    category: CategoryRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    print(category)
    category_obj = crud.category.update(
        db, obj_in=category, user_id=current_user.id
    )
    if category is not None:
        category_schema = CategoryRequest(id=category_obj.id, name=category_obj.name)
        return CategoryResponse(
            categories=[category_schema],
            message="Success",
            status=str(status.HTTP_200_OK),
        )
    else:
        return CategoryResponse(
            message="Category not found",
            status=str(status.HTTP_404_NOT_FOUND),
            categories=[],
        )