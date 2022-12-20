from app.crud.base import CRUDBase
from app.models.activity_log import ActivityLog
from app.schemas import ActivityLogCreate, ActivityLogUpdate


class CRUDActivityLog(CRUDBase[ActivityLog, ActivityLogCreate, ActivityLogUpdate]):
    ...


activity_log = CRUDActivityLog(ActivityLog)
