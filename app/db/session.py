from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For tests purpose

engine_test = create_engine(settings.SQLALCHEMY_TEST_DATABASE_URI, pool_pre_ping=True)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


# MongoDB sessions
mongo_client = MongoClient(settings.MONGO_DATABASE_URI)
