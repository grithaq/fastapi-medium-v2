from pydantic import BaseModel
from .base import ResponseModel
from typing import TypeVar, List


T = TypeVar


class CategoryRequest(BaseModel):
    id: int
    name: str


class CategoryResponse(ResponseModel):
    categories: List = [T]