from fastapi import APIRouter, Body, Depends, HTTPException, status
from src.core.database import get_repository
from src.core.permissions import get_user_scopes
from src.models.schemas.users import UserCreate, UserForResponse, UserInLogin, UserWithToken
from src.repositories.users import UserRepository
from src.services.jwt import create_access_token


router = APIRouter()


@router.post("/register", response_model=UserForResponse)
async def create_user(
    user: UserCreate, user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    db_user = user_repo.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repo.create_user(user=user)


@router.post("/login", response_model=UserWithToken)
async def login(
    user_login: UserInLogin = Body(...),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    user = user_repo.get_user_by_email(user_login.email.lower())
    if not user or not user.check_password(user_login.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    scopes = await get_user_scopes(user)
    access_token = await create_access_token(data={"sub": str(user.id), "scopes": scopes})
    return {"access_token": access_token, "token_type": "bearer"}
