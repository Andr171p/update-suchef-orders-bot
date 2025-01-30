from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.database.manager import DatabaseManager

from sqlalchemy import select

from src.database.interfaces import BaseCRUD
from src.database.provider import get_database_manager
from src.database.models import User


class UserCRUD(BaseCRUD):
    def __init__(
            self,
            manager: "DatabaseManager" = get_database_manager()
    ) -> None:
        self._manager = manager

    async def create(self, user: User) -> User | None:
        async with self._manager.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def read_by_user_id(self, user_id: int) -> User | None:
        async with self._manager.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_by_phone(self, phone: str) -> User | None:
        async with self._manager.session() as session:
            stmt = (
                select(User)
                .where(User.phone == phone)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_all(self) -> Sequence[User]:
        async with self._manager.session() as session:
            stmt = select(User)
            users = await session.execute(stmt)
        return users.scalars().all()

    async def update(self, user: User) -> User | None:
        async with self._manager.session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def delete(self, user_id: int) -> User | None:
        async with self._manager.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
            if user:
                await session.delete(user)
                await session.commit()
        return user.scalar_one_or_none()
