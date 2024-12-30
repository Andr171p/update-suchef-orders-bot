from typing import Any, Sequence
from functools import singledispatchmethod

from sqlalchemy import select

from src.database.context import DBSession
from src.database.models.user import User


class UserService(DBSession):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_users(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(User.metadata.drop_all)
            await connection.run_sync(User.metadata.create_all)

    async def add_user(self, user: User) -> User | None:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def update_user(self, user: User) -> User | None:
        async with self.session() as session:
            await session.merge(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> User:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
            if user:
                await session.delete(user)
                await session.commit()
            return user.scalar_one_or_none()

    @singledispatchmethod
    async def get_user(self, arg: Any) -> User | None:
        raise NotImplementedError("<UserService> `get_user` method not implement...")

    @get_user.register
    async def _(self, user_id: int) -> User | None:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
            try:
                return user.scalar_one_or_none()
            except Exception as _ex:
                raise _ex

    @get_user.register
    async def _(self, phone: str) -> User | None:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.phone == phone)
            )
            user = await session.execute(stmt)
            try:
                return user.scalar_one_or_none()
            except Exception as _ex:
                raise _ex

    async def get_users(self) -> Sequence[User]:
        async with self.session() as session:
            stmt = select(User)
            users = await session.execute(stmt)
            return users.scalars().all()


user_service = UserService()
