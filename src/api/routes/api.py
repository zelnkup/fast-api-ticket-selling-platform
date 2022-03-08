from fastapi import APIRouter
from src.api.routes import authentication, users


router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/users")
router.include_router(authentication.router, tags=["auth"], prefix="/auth")
