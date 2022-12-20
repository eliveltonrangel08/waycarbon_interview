import json
from typing import Any

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.api import deps
from app.core import security
from app import crud, models, schemas
from app.schemas import ActivityLogCreate

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    crud.activity_log.create(obj_in=ActivityLogCreate(
        type="login_request",
        logged_user_id=user.id,
    ))

    return schemas.Token(
        access_token=security.create_access_token(user.id),
        token_type="bearer"
    ).dict()


@router.post("/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    crud.activity_log.create(obj_in=ActivityLogCreate(
        type="test_token",
        logged_user_id=current_user.id,
    ))
    return current_user
