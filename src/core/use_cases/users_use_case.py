from src.core.entities import User


class UsersUseCase:

    async def register(self, user: User) -> bool:
        ...

    async def verify(self, user_id: int) -> bool:
        ...
