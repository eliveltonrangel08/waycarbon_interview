from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ActivityLog(Base):
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), index=True)
    logged_user = Column(String(255), index=True)
    json_data = Column(JSON)
    user_ip = Column(String(64))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    logged_user_id = Column(Integer, ForeignKey("user.id"))
    logged_user = relationship("User", back_populates="logs", uselist=False, lazy="select")
