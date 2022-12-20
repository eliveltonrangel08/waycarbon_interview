from fastapi.encoders import jsonable_encoder

from app import crud
from app.schemas import UserCreate
from app.test.utils.utils import random_email, random_lower_string


def test_create_user() -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(obj_in=user_in)

    assert hasattr(user, "hashed_password")


def test_authenticate_user() -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(obj_in=user_in)
    authenticated_user = crud.user.authenticate(email=email, password=password)

    assert authenticated_user.email == user.email


def test_not_authenticate_user() -> None:
    email = random_email()
    password = random_lower_string()
    authenticated_user = crud.user.authenticate(email=email, password=password)

    assert authenticated_user is None


def test_get_user(user_factory) -> None:
    user = user_factory(username="user_get@test.com")
    user_get = crud.user.get(id=user.id)

    assert user.email == user_get.email
    assert jsonable_encoder(user) == jsonable_encoder(user_get)
