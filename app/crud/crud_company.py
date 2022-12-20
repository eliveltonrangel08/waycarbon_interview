from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas import CompanyCreate, CompanyUpdate


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    ...


company = CRUDCompany(Company)
