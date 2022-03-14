from fastapi import Depends, HTTPException
from fastapi.requests import Request
from fastapi.security import SecurityScopes
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from src.core.database import get_repository
from src.core.exceptions import AuthHTTPException
from src.core.settings import settings
from src.repositories.users import UserRepository
from starlette import status


async def get_current_user(
    request: Request,
    security_scopes: SecurityScopes,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    """
    Verifies auth token and assigns user to request.state object
    """
    authorization = request.headers.get("Authorization")
    scheme, token = get_authorization_scheme_param(authorization)
    if not (authorization and scheme and token):
        raise AuthHTTPException("Provide Bearer token")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")
        user_scopes: list = payload.get("scopes")
        if not user_id:
            raise AuthHTTPException()
    except JWTError as exc:
        raise AuthHTTPException(str(exc))

    user = user_repo.get_user_by_id(user_id)
    if not user:
        raise AuthHTTPException()

    # Check permissions
    for scope in security_scopes.scopes:
        if scope not in user_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": "Bearer"},
            )

    request.state.user = user
    return user
