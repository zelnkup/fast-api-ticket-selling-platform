from datetime import datetime, timedelta

from jose import jwt
from src.core.settings import settings


async def create_access_token(data: dict):
    to_encode = data.copy()
    expire_at = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_at})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
