import uvicorn as uvicorn
from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.db.admin import UserAdmin
from app.db.session import engine

app = FastAPI(
    title="Interview API Example", openapi_url="/api/v1/openapi.json"
)
admin = Admin(app, engine)

# App settings
app.include_router(api_router, prefix="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Admin settings
admin.add_view(UserAdmin)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
