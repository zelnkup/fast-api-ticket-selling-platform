import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))

    DATABASE_URL: str = "postgresql://debug:debug@db:5432/debug"

    CORS_ORIGINS = [
        "http://localhost",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
