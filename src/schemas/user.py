from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None
