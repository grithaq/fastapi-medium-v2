from fastapi import APIRouter

from api.api_v1.endpoints import category

api_router = APIRouter()

api_router.include_router(category.router, tags=['category'], prefix='/category')