from typing import List

from app.crud.mongo.base import CRUDBase
from app.schemas.mongo import DocumentsCreate, DocumentsUpdate, Documents


class CRUDDocuments(CRUDBase[Documents, DocumentsCreate, DocumentsUpdate]):
    def get_multi_by_company(
            self, *, company_id: int, skip: int = 0, limit: int = 100
    ) -> List[Documents]:
        db_collection = self.db_session[self.collection_name]
        _documents = db_collection.find({"company_id": company_id})
        documents_obj_list = [self.model(**document) for document in _documents]
        return documents_obj_list


documents = CRUDDocuments(Documents, "documents")
