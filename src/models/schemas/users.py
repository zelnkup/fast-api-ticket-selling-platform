from pydantic import BaseConfig, BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserForResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserWithToken(BaseModel):
    access_token: str


class UserInLogin(BaseModel):
    email: EmailStr
    password: str

    class Config(BaseConfig):
        orm_mode = True
        allow_population_by_field_name = True
