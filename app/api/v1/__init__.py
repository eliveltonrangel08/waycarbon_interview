from fastapi import APIRouter
from . import login, user, documents

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
