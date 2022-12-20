from app.crud.mongo.base import CRUDBase
from app.schemas.mongo import DocumentsCreate, DocumentsUpdate, Documents


class CRUDDocuments(CRUDBase[Documents, DocumentsCreate, DocumentsUpdate]):
    ...


documents = CRUDDocuments(Documents, "documents")
