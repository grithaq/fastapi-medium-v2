from fastapi import APIRouter
from src.schemas.category import CategoryRequest, CategoryResponse

router = APIRouter()


@router.post("/",)
def create_category(
    category: CategoryRequest
):
    category = CategoryRequest(
        id=category.id,
        name=category.name
    )
    category_response = CategoryResponse(
        status="201",
        message="Success",
        categories=[category]
    )
    return category_response