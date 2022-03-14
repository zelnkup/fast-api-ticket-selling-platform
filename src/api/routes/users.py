from fastapi import APIRouter, Depends, HTTPException, Security
from src.core.database import get_repository
from src.core.dependencies import get_current_user
from src.models.schemas.users import UserForResponse
from src.repositories.users import User, UserRepository


router = APIRouter()


@router.get("/", response_model=list[UserForResponse])
async def get_users(
    offset: int = 0,
    limit: int = 100,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
    current_user: User = Security(get_current_user, scopes=["admin"]),
):
    users = user_repo.get_users(offset=offset, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserForResponse)
async def get_user(
    user_id: int,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
    current_user: User = Depends(get_current_user),
):
    user = user_repo.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
