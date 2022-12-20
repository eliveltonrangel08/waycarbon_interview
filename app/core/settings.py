import secrets
from enum import Enum
from typing import Optional, Dict, Any

from pydantic import BaseSettings, validator, AnyHttpUrl


class Environments(str, Enum):
    PRODUCTION = 'PRODUCTION'
    TEST = 'TEST'
    DEVELOPMENT = 'DEVELOPMENT'


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 5 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 5
    SERVER_NAME: str = 'localhost'
    SERVER_HOST: AnyHttpUrl = 'http://localhost'

    ENVIRONMENT_APP: Environments = Environments.DEVELOPMENT

    MONGO_SERVER: str = '0.0.0.0'
    MONGO_USER: str = 'root'
    MONGO_PASSWORD: str = 'toor'
    MONGO_DB: str = 'interview'

    MYSQL_SERVER: str = '0.0.0.0'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'toor'
    MYSQL_DB: str = 'interview'
    SQLALCHEMY_DATABASE_URI: Optional[Any] = None
    SQLALCHEMY_TEST_DATABASE_URI: Optional[Any] = None
    MONGO_DATABASE_URI: Optional[Any] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        user = values.get("MYSQL_USER")
        password = values.get("MYSQL_PASSWORD")
        host = values.get("MYSQL_SERVER")
        db = values.get("MYSQL_DB")
        return f"mysql+pymysql://{user}:{password}@{host}/{db}"

    @validator("SQLALCHEMY_TEST_DATABASE_URI", pre=True)
    def assemble_test_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        user = values.get("MYSQL_USER")
        password = values.get("MYSQL_PASSWORD")
        host = values.get("MYSQL_SERVER")
        db = f"test_{values.get('MYSQL_DB')}"
        return f"mysql+pymysql://{user}:{password}@{host}/{db}"

    @validator("MONGO_DATABASE_URI", pre=True)
    def assemble_mongo_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        user = values.get("MONGO_USER")
        password = values.get("MONGO_PASSWORD")
        host = values.get("MONGO_SERVER")
        return f"mongodb://{user}:{password}@{host}"

    class Config:
        case_sensitive = True


settings = Settings()
