from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud
from api.deps import get_current_user, get_db
from db.models import User
from utils import pagination
from src.schemas.category import (CategoryCreate, CategoryRequest,
                                  CategoryResponse, CategorySchema,
                                  ResponseModel, ListCategoryRespose)

router = APIRouter()


@router.get("/")
def get_category(
    page: int = 1,
    per_page: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    categories = crud.category.get_all_by_user_id(db, user_id=current_user.id)
    categories = pagination.paginate(
        items=categories, page=page, per_page=per_page
    )
    items = [
        CategorySchema(user_id=category.user_id, id=category.id, name=category.name)
        for category in categories['items']
    ]
    return ListCategoryRespose(
        message="Success", status=str(status.HTTP_200_OK), data=items,
        current=categories['current'], total=categories['total']
    )


@router.post(
    "/",
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category_obj = crud.category.create(db, obj_in=category, user_id=current_user.id)
    category_schema = CategorySchema(id=category_obj.id, name=category_obj.name, user_id=category_obj.user_id)
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
    category_obj = crud.category.update(db, obj_in=category, user_id=current_user.id)
    if category is not None:
        category_schema = CategorySchema(id=category_obj.id, name=category_obj.name, user_id=category_obj.user_id)
        return CategoryResponse(
            message="Success",
            status=str(status.HTTP_200_OK),
            data=[category_schema]
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
    crud.category.delete(db, id=int(category_id), user_id=current_user.id)
    return ResponseModel(
        message="Success",
        status=str(status.HTTP_200_OK),
    )
