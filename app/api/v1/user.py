from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app import schemas, crud, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.User], dependencies=[Depends(deps.get_current_active_superuser)])
def read_users(
        *,
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Read a list of all users based on paginator.
    """
    users = crud.user.get_multi(skip=skip, limit=limit)
    return users


@router.get("/me", response_model=schemas.User)
def read_users(
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Returns the current User
    """
    return current_user


@router.post("/", response_model=schemas.User, dependencies=[Depends(deps.get_current_active_superuser)])
def create_user(
        *,
        user_in: schemas.UserCreate
) -> Any:
    """
    Create a new user
    """
    user = crud.user.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system"
        )
    user = crud.user.create(obj_in=user_in)
    return user


@router.put("/", response_model=schemas.User, dependencies=[Depends(deps.get_current_active_superuser)])
def update_user(
        *,
        user_id: int,
        user_in: schemas.UserUpdate
) -> Any:
    """
    Update an existing user
    """
    user = crud.user.get(id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exists in the system"
        )
    user = crud.user.update(db_obj=user, obj_in=user_in)
    return user


@router.delete("/", response_model=schemas.User, dependencies=[Depends(deps.get_current_active_superuser)])
def update_user(
        user_id: int
) -> Any:
    """
    Delete an existing user given a user_id
    """
    user = crud.user.get(id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exists in the system"
        )
    user = crud.user.remove(id=user_id)
    return user
