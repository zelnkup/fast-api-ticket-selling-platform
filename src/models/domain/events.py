from sqlalchemy import Boolean, Column, DateTime, Integer, String
from src.core.database import Base


class Event(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_active = Column(Boolean)
    start_at = Column(DateTime)
