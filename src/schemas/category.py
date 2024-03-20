from typing import List, TypeVar

from pydantic import BaseModel

from .base import ResponseModel

T = TypeVar


class CategoryRequest(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str


class CategoryResponse(ResponseModel):
    data: List = [T]


class CategorySchema(CategoryRequest):
    user_id: int


class ListCategoryRespose(ResponseModel):
    current: int
    total: int
    data: List = [T]