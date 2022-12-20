from typing import Optional, Dict, Any

from bson import ObjectId
from fastapi import File, UploadFile
from pydantic import BaseModel, Field


class DocumentsBase(BaseModel):
    description: Optional[str] = None
    metadata: Optional[Dict] = None
    metadata_file: Optional[Dict] = None


# Properties to receive via API on creation
class DocumentsCreate(DocumentsBase):
    user_id: int = Field(..., hidden=True)
    company_id: int = Field(..., hidden=True)
    raw_file: Optional[Any] = None
    ...


# Properties to receive via API on update
class DocumentsUpdate(DocumentsBase):
    ...


class DocumentsInDBBase(DocumentsBase):
    # id: Optional[Any] = Field(alias="_id")
    user_id: Optional[int] = None
    company_id: Optional[int] = None


# Additional properties to return via API
class Documents(DocumentsInDBBase):
    ...
