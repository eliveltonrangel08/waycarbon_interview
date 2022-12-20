from datetime import datetime
from typing import TypeVar, Generic, Type, Any, Optional, List, Dict, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from app.core.settings import settings
from app.db.session import mongo_client

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


def get_db():
    try:
        db = mongo_client[settings.MONGO_DB]
        yield db
    finally:
        pass
        # db.close()


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], collection_name):
        self.model = model
        self.collection_name = collection_name
        self.db_session = next(get_db())

    def get(self, id: Any) -> Optional[ModelType]:
        db_collection = self.db_session[self.collection_name]
        return db_collection.find_one({"_id": id})

    def get_multi(
            self, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        db_collection = self.db_session[self.collection_name]
        documents = db_collection.find()
        return documents

    def create(self, *, obj_in: Union[Dict, CreateSchemaType]) -> ModelType:
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.dict(exclude_unset=True)
        create_data["created_at"] = datetime.utcnow()

        db_collection = self.db_session[self.collection_name]
        db_obj = db_collection.insert_one(create_data)
        print(db_obj)
        return db_obj

    def update(
            self, *, obj_id: int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        update_data["updated_at"] = datetime.utcnow()

        db_collection = self.db_session[self.collection_name]
        db_obj = db_collection.find_one_and_update({"_id": obj_id}, **update_data)
        return db_obj

    def remove(self, *, id: int) -> ModelType:
        db_collection = self.db_session[self.collection_name]
        db_obj = db_collection.delete_one({"_id": id})
        return db_obj
