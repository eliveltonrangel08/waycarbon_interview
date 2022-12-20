from typing import List, Any, Optional

from fastapi import APIRouter, Depends, UploadFile, File

from app.api import deps
from app.crud import mongo as crud_mongo
from app.schemas import mongo as schemas_mongo

router = APIRouter()


# @router.get("/", response_model=List[schemas_mongo.Documents], dependencies=[Depends(deps.get_current_active_superuser)])
@router.get("/", response_model=List[schemas_mongo.Documents])
def read_documents(
        *,
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Read a list of all documents based on paginator.
    """
    documents = crud_mongo.documents.get_multi(skip=skip, limit=limit)
    print(list(documents))
    return list(documents)


@router.post("/", response_model=schemas_mongo.Documents)
# @router.post("/", response_model=schemas_mongo.Documents, dependencies=[Depends(deps.get_current_active_superuser)])
def create_document(
        *,
        document_in: schemas_mongo.DocumentsCreate = Depends(schemas_mongo.DocumentsCreate),
        file: Optional[UploadFile] = File(...)
) -> Any:
    """
    Create a new user
    """
    user = crud_mongo.documents.create(obj_in=document_in)
    return user
