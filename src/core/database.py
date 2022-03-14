from typing import Callable, Dict, Type

from fastapi import Depends
from pydantic import Field
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session, sessionmaker
from src.core.settings import settings
from src.repositories.base import BaseRepository


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: int = Field(0, alias="id")
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_repository(repo_type: Type[BaseRepository]) -> Callable[[Session], BaseRepository]:
    """
    Returns repository with active db session
    """

    def _get_repo(session: Session = Depends(get_db)) -> BaseRepository:
        return repo_type(session)

    return _get_repo
