from fastapi import APIRouter
from src.schemas.category import CategoryReqeust

router = APIRouter()


@router.post("/",)
def create_category(
    category: CategoryReqeust
):
    return category