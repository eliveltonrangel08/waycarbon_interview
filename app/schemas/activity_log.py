from typing import Optional, Dict

from pydantic import BaseModel


# Shared properties
class ActivityLogBase(BaseModel):
    type: Optional[str] = None
    logged_user_id: int = None
    json_data: Optional[Dict] = None
    user_ip: Optional[str] = None


# Properties to receive via API on creation
class ActivityLogCreate(ActivityLogBase):
    ...


# Properties to receive via API on update
class ActivityLogUpdate(ActivityLogBase):
    ...


class ActivityLogInDBBase(ActivityLogBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ActivityLog(ActivityLogInDBBase):
    ...

