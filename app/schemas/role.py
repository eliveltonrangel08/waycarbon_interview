from typing import Optional

from pydantic import BaseModel, Json


# Shared properties
from .company import Company


class RoleBase(BaseModel):
    name: str = None
    alias: Optional[str] = None
    description: Optional[str] = None
    settings: Optional[Json] = None
    company_id: int = None


# Properties to receive via API on creation
class RoleCreate(RoleBase):
    ...


# Properties to receive via API on update
class RoleUpdate(RoleBase):
    ...


class RoleInDBBase(RoleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Role(RoleInDBBase):
    company: Company = None

