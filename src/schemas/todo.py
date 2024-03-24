from typing import List

from .base import BaseModel, ResponseModel, T
from .category import CategoryRequest


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


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    category: CategoryRequest


class ListTodoResponse(ResponseModel):
    current: int
    total: int
    data: List[TodoSchema]
