from typing import Any

from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


class APIException(Exception):
    """
    initializing object exception leads to response
    with status_code, error_code and message
    """

    def __init__(
        self, error_code: int = 000, status_code: int = 500, detail="", message="", *args, **kwargs,
    ):
        Exception.__init__(self, *args, **kwargs)

        self.error_code = error_code
        self.message = message
        self.detail = detail
        self.status_code = status_code

    def __str__(self):
        return f"APIException(status_code={self.status_code}, detail={self.message})"


async def on_api_exception(request: Request, exception: APIException) -> JSONResponse:
    content = {"error": {"error_code": exception.error_code}}

    if exception.message:
        content["error"]["message"] = exception.message

    if exception.detail:
        content["error"]["detail"] = exception.detail

    return JSONResponse(content=content, status_code=exception.status_code)


class AuthHTTPException(StarletteHTTPException):
    status_code = 401
    detail = "Could not validate credentials"
    headers = {"WWW-Authenticate": "Bearer"}

    def __init__(self, detail: Any = None,) -> None:
        super().__init__(status_code=self.status_code, detail=detail or self.detail)
