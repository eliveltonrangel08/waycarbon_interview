from typing import List, Any, Optional

from fastapi import APIRouter, Depends, UploadFile, File

from app import models
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


# @router.get("/", response_model=List[schemas_mongo.Documents], dependencies=[Depends(deps.get_current_active_user)])
@router.get("/company", response_model=List[schemas_mongo.Documents])
def read_company_documents(
        *,
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Read a list of all documents owned by company based on paginator.
    """
    company_id = current_user.role.company_id
    documents = crud_mongo.documents.get_multi_by_company(company_id=company_id, skip=skip, limit=limit)
    print(list(documents))
    return list(documents)


@router.post("/", response_model=schemas_mongo.Documents)
# @router.post("/", response_model=schemas_mongo.Documents, dependencies=[Depends(deps.get_current_active_superuser)])
def create_document(
        *,
        document_in: schemas_mongo.DocumentsBase = Depends(schemas_mongo.DocumentsBase),
        file: Optional[UploadFile] = File(...),
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create a new user
    """
    document_to_create = schemas_mongo.DocumentsCreate(
        **document_in.dict(),
        user_id=current_user.id,
        company_id=current_user.role.company_id
    )
    user = crud_mongo.documents.create(obj_in=document_to_create)
    return user
