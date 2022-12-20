from typing import TypeVar, Generic, Type, Any, Optional, List, Dict, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.settings import settings, Environments
from app.db.base_class import Base
from app.db.session import SessionLocal, SessionLocalTest

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


def get_db():
    try:
        if settings.ENVIRONMENT_APP == Environments.TEST:
            db = SessionLocalTest()
        else:
            db = SessionLocal()
        yield db
    finally:
        db.close()


def save(db: Session, db_obj: ModelType):
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.db_session = next(get_db())

    def get(self, id: Any) -> Optional[ModelType]:
        return self.db_session.query(self.model).filter(self.model.id == id).first()

    def get_multi(
            self, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return self.db_session.query(self.model).order_by(self.model.id).offset(skip).limit(limit).all()

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data)
        save(self.db_session, db_obj)
        return db_obj

    def update(
            self, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        save(self.db_session, db_obj)
        return db_obj

    def remove(self, *, id: int) -> ModelType:
        obj = self.db_session.query(self.model).get(id)
        self.db_session.delete(obj)
        self.db_session.commit()
        return obj
