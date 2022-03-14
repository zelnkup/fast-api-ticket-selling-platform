import datetime

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    start_at: datetime.datetime


class EventInResponse(EventBase):
    id: int
    is_active: bool
