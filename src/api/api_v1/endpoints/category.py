from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import repositories
from api.deps import get_current_user, get_db
from db.models import User
from src.schemas.category import (CategoryCreate, CategoryRequest,
                                  CategoryResponse, CategorySchema,
                                  ListCategoryRespose, ResponseModel)

router = APIRouter()


@router.get("/")
def get_category(
    page: int = 1,
    per_page: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    categories = repositories.category.get_all_by_user_id(
        db, user_id=current_user.id, per_page=per_page, page=page
    )
    total_data = repositories.category.count_data_by_user_id(
        db, user_id=current_user.id
    )
    items = [
        CategorySchema(user_id=category.user_id, id=category.id, name=category.name)
        for category in categories
    ]
    return ListCategoryRespose(
        message="Success",
        status=str(status.HTTP_200_OK),
        data=items,
        current=page,
        total=total_data,
    )


@router.post(
    "/",
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category_obj = repositories.category.create(
        db, obj_in=category, user_id=current_user.id
    )
    category_schema = CategorySchema(
        id=category_obj.id, name=category_obj.name, user_id=category_obj.user_id
    )
    return CategoryResponse(
        data=[category_schema],
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
    category_obj = repositories.category.update(
        db, obj_in=category, user_id=current_user.id
    )
    if category is not None:
        category_schema = CategorySchema(
            id=category_obj.id, name=category_obj.name, user_id=category_obj.user_id
        )
        return CategoryResponse(
            message="Success", status=str(status.HTTP_200_OK), data=[category_schema]
        )
    else:
        return CategoryResponse(
            message="Category not found",
            status=str(status.HTTP_404_NOT_FOUND),
            categories=[],
        )


@router.delete("/{category_id}")
def delete_category(
    category_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repositories.category.delete(db, id=int(category_id), user_id=current_user.id)
    return ResponseModel(
        message="Success",
        status=str(status.HTTP_200_OK),
    )
