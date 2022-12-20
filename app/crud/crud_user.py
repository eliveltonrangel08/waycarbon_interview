from typing import Optional

from app.api import deps
from app.core.security import verify_password, get_password_hash
from app.crud.base import CRUDBase, save
from app.models.user import User
from app.schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, *, email: str) -> Optional[User]:
        return self.db_session.query(self.model).filter(self.model.email == email).first()

    def authenticate(self, *, email: str, password: str) -> Optional[User]:
        # TODO: just for development purpose
        if 'admin' == email == password:
            return deps.get_default_user_admin()

        _user = self.get_by_email(email=email)
        if not _user:
            return
        if not verify_password(password, _user.hashed_password):
            return

        return _user

    def create(self, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            role_id=obj_in.role_id
        )
        save(self.db_session, db_obj)
        return db_obj


user = CRUDUser(User)
