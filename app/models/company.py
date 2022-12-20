from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, func, DateTime
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Company(Base):
    id = Column(Integer, primary_key=True, index=True)
    is_enabled = Column(Boolean(), default=True)
    name = Column(String(255), index=True)
    nickname = Column(String(255))
    area = Column(String(255))
    code_number = Column(String(128))
    address_street = Column(String(128))
    address_number = Column(String(128))
    address_neighborhood = Column(String(128))
    address_code = Column(String(64))
    address_city = Column(String(128))
    address_country = Column(String(128))
    contact = Column(String(64))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    roles = relationship("Role", back_populates="company")


CompanySchema = sqlalchemy_to_pydantic(Company)
