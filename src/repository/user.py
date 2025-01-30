from typing import List

from src.repository.base import BaseRepository
from src.database.models import User
from src.database.crud import UserCRUD
from src.schemas.user import UserSchema


class UserRepository(BaseRepository):
    _crud = UserCRUD()

    async def add(self, user: UserSchema) -> UserSchema:
        added_user = await self._crud.create(User(**user.model_dump()))
        return UserSchema(**added_user.__dict__)

    async def get_all(self) -> List[UserSchema] | None:
        users = await self._crud.read_all()
        if users is None:
            return
        return [UserSchema(**user.__dict__) for user in users]

    async def get_by_user_id(self, user_id: int) -> UserSchema | None:
        user = await self._crud.read_by_user_id(user_id)
        if user is None:
            return
        return UserSchema(**user.__dict__)
