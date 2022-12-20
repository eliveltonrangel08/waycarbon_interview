from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Role(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    alias = Column(String(255))
    description = Column(String(255), nullable=True)
    settings = Column(JSON)

    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="roles")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    users = relationship("User", back_populates="role")

    # __mapper_args__ = {
    #     "order_by": id
    # }

    class Meta:
        ordered = True
        fields = id
