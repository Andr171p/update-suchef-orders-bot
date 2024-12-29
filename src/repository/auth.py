from typing import Optional

from src.database.models.user import User
from src.database.service.user import UserService

from src.schemas.user import UserSchema


class AuthRepository:
    user_service: UserService = UserService()

    @classmethod
    async def register_user(
            cls,
            user_id: int,
            username: Optional[str],
            phone: str
    ) -> User:
        user = UserSchema(**locals())
        registered_user = await cls.user_service.add_user(User(**user.__dict__))
        return registered_user


auth_repository = AuthRepository()
