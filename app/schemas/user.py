from typing import Optional

from pydantic import BaseModel, EmailStr
# from pydantic_sqlalchemy import sqlalchemy_to_pydantic
#
# from app.models.user import User


# UserSchema = sqlalchemy_to_pydantic(User)


# Shared properties
from .role import Role


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: bool = None
    full_name: Optional[str] = None
    role_id: Optional[int] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    role: Role = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
