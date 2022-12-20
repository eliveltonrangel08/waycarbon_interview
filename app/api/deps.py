import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from starlette import status

from app import schemas, crud, models
from app.core import security
from app.core.settings import settings
from app.db.session import SessionLocal
from app.models import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/v1/login/access-token"
)


def get_current_user(
        token: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )

    if token_data.sub == -9999:
        return get_default_user_admin()

    user = crud.user.get(id=token_data.sub)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def get_current_active_user(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user


def get_current_active_superuser(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not current_user.is_active and current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user does not have enough privileges")
    return current_user


def get_default_user_admin():
    return User(
        id=-9999,
        is_active=True,
        is_superuser=True,
        email="test@test.com",
        full_name="USER ADMIN DEVELOPMENT"
    )
