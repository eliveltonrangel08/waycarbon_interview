from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.activity_log import ActivityLog
from app.models.role import Role


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    role_id = Column(Integer, ForeignKey("role.id"), nullable=True)
    role = relationship(Role, back_populates="users", uselist=False, lazy="select")

    logs = relationship(ActivityLog, back_populates="logged_user")
