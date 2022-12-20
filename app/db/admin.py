from sqladmin import ModelView

from app.models import User


class UserAdmin(ModelView, model=User):
    column_exclude_list = [User.hashed_password]
