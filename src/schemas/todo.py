from typing import List

from .base import BaseModel, ResponseModel, T


class TodoRequest(BaseModel):
    title: str
    description: str
    category_id: int


class TodoCreate(BaseModel):
    title: str
    description: str
    category_id: int


class TodoUpdate(BaseModel):
    title: str
    description: str
    category_id: int


class TodoResponse(ResponseModel):
    data: List[T]
