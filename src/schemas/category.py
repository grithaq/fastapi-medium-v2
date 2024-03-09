from pydantic import BaseModel


class CategoryReqeust(BaseModel):
    id: int
    name: str