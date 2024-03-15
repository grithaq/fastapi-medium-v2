from typing import List, TypeVar

from pydantic import BaseModel

from .base import ResponseModel

T = TypeVar


class CategoryRequest(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    id: int
    name: str


class CategoryUpdate(BaseModel):
    name: str


class CategoryResponse(ResponseModel):
    categories: List = [T]
