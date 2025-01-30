import logging

from src.repository import UserRepository
from src.schemas import UserSchema


log = logging.getLogger(__name__)


class UserService:
    _repository = UserRepository()

    async def register(self, user: UserSchema) -> None:
        register_user = await self._repository.add(user)
        log.info("Successfully register %s", register_user)

    async def verify(self, user_id: int) -> bool:
        user = await self._repository.get_by_user_id(user_id)
        return True if user is not None else False
