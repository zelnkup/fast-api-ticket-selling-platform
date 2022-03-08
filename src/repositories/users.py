from src.models.domain.users import User
from src.models.schemas.users import UserCreate
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self, offset: int = 0, limit: int = 100):
        return self.db.query(User).offset(offset).limit(limit).all()

    def create_user(self, user: UserCreate):
        db_user = User(email=user.email)
        db_user.set_password(user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
