from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.api import router as api_router
from src.core.database import SessionLocal
from src.core.exceptions import APIException, on_api_exception
from src.core.settings import settings


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(api_router, prefix="/api")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )
    application.add_exception_handler(APIException, on_api_exception)

    return application


app = get_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
