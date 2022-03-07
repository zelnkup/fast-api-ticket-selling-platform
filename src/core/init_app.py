from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.exceptions import APIException, on_api_exception
from src.core.settings import settings
from src.users.routes import router as users_router


def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )


def register_routers(app: FastAPI):
    app.include_router(users_router, prefix="/api/users")


def register_exceptions(app: FastAPI):
    app.add_exception_handler(APIException, on_api_exception)
