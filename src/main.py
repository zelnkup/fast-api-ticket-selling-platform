from fastapi import FastAPI, Request, Response
from src.core.database import SessionLocal
from src.core.init_app import init_middlewares, register_exceptions, register_routers

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


init_middlewares(app)
register_exceptions(app)
register_routers(app)
