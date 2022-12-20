from typing import Optional, Dict, Any

from fastapi import File, UploadFile
from pydantic import BaseModel


class DocumentsBase(BaseModel):
    user_id: int
    description: Optional[str] = None
    metadata: Optional[Dict] = None
    metadata_file: Optional[Dict] = None
    raw_file: Optional[Any] = None


# Properties to receive via API on creation
class DocumentsCreate(DocumentsBase):
    ...


# Properties to receive via API on update
class DocumentsUpdate(DocumentsBase):
    ...


class DocumentsInDBBase(DocumentsBase):
    id: Optional[int] = None


# Additional properties to return via API
class Documents(DocumentsInDBBase):
    ...
