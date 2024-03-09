from fastapi import FastAPI
from src.api.api_v1.api import api_router
from src.core.config import settings


def crate_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    application.include_router(api_router, prefix=settings.API_V1_STR)
    return application


app = crate_application()
