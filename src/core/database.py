from typing import Callable, Type

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from src.core.settings import settings
from src.repositories.base import BaseRepository


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_repository(repo_type: Type[BaseRepository],) -> Callable[[Session], BaseRepository]:
    """
    Returns repository with active db session
    """

    def _get_repo(session: Session = Depends(get_db),) -> BaseRepository:
        return repo_type(session)

    return _get_repo
