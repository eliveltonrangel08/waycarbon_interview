from typing import Optional, Dict

from pydantic import BaseModel


# Shared properties
class CompanyBase(BaseModel):
    is_enabled: Optional[bool] = True
    name: str = None
    nickname: Optional[str] = None
    area: Optional[str] = None
    code_number: Optional[str] = None
    address_street: Optional[str] = None
    address_number: Optional[str] = None
    address_neighborhood: Optional[str] = None
    address_code: Optional[str] = None
    address_city: Optional[str] = None
    address_country: Optional[str] = None
    contact: Optional[str] = None


# Properties to receive via API on creation
class CompanyCreate(CompanyBase):
    ...


# Properties to receive via API on update
class CompanyUpdate(CompanyBase):
    ...


class CompanyInDBBase(CompanyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Company(CompanyInDBBase):
    ...

