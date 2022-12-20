from typing import Generator

import pytest
from mixer.backend.sqlalchemy import Mixer
from fastapi.testclient import TestClient

from app import crud
from app.core.security import get_password_hash
from app.db.session import SessionLocalTest
from app.models import User
from app.test.utils.utils import random_lower_string
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocalTest()


@pytest.fixture(scope="session")
def mixer() -> Mixer:
    return Mixer(session=SessionLocalTest, commit=True)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


# User fixtures
@pytest.fixture(scope="session")
def user_factory(db: Generator):
    def factory(username: str, is_superuser: bool = False, is_active: bool = True):
        user = crud.user.get_by_email(email=username)
        if not user:
            user = User(
                email=username,
                hashed_password=get_password_hash(random_lower_string()),
                full_name=random_lower_string(),
                is_active=is_active,
                is_superuser=is_superuser
            )
        else:
            user.is_superuser = is_superuser
            user.is_active = is_active
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    return factory





