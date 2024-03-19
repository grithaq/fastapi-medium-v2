from fastapi import APIRouter

from api.api_v1.endpoints import category, login, todo

api_router = APIRouter()

api_router.include_router(login.router, tags=["Login"])
api_router.include_router(category.router, tags=["category"], prefix="/category")
api_router.include_router(todo.router, tags=["todo"], prefix="/todo")
