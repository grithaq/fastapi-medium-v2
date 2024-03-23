from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel):
    status: str
    message: str