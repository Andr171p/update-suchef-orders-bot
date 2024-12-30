import logging

from typing import Optional

from src.database.models.user import User
from src.database.service.user import UserService

from src.schemas.user import UserSchema


log = logging.getLogger(__name__)


class UserRepository:
    user_service: UserService = UserService()

    @classmethod
    async def add_user(
            cls,
            user_id: int,
            username: Optional[str],
            phone: str
    ) -> User:
        user = UserSchema(**locals())
        registered_user = await cls.user_service.add_user(User(**user.__dict__))
        log.info("User %s register successfully", user_id)
        return registered_user

    @classmethod
    async def get_user(cls, user_id: int) -> User:
        user = await cls.user_service.get_user(user_id)
        log.info("Found user %s", user)
        return user

    @classmethod
    async def check_user_exists(cls, user_id: int) -> bool:
        user = await cls.user_service.get_user(user_id)
        log.info("Found user %s", user)
        return True if user is not None else False


user_repository = UserRepository()
