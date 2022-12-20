from typing import Dict

from app import crud
from app.models import User
from app.schemas import UserCreate, UserUpdate
from app.test.utils.utils import random_email, random_lower_string

from fastapi.testclient import TestClient


def user_authentication_headers(
        *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email, "password": password}
    response = client.post("/api/v1/login/access-token", data=data).json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def create_random_user() -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(obj_in=user_in)
    return user


def authentication_token_from_email(
        *, client: TestClient, email: str
) -> Dict[str, str]:
    """
    Return a valid token for the user with given email or creates a new user if it is not available.
    """
    password = random_lower_string()
    user = crud.user.get_by_email(email=email)
    if not user:
        user_in = UserCreate(username=email, email=email, password=password)
        crud.user.create(user_in)
    else:
        user_update = UserUpdate(password=password)
        crud.user.update(user_update, db_obj=user, obj_in=user_update)
    return user_authentication_headers(client=client, email=email, password=password)
