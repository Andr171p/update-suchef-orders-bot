from src.database.service.user import UserService
from src.http.client import HTTPClient
from src.http.response import JsonResponse
from src.service.flyers import FlyersService
from src.schemas.flyers import FlyersSchema


class FlyersRepository:
    user_service = UserService()
    http_client = HTTPClient(JsonResponse())
    flyers_service = FlyersService(http_client)

    @classmethod
    async def get_flyers(cls, user_id: int) -> FlyersSchema:
        user = await cls.user_service.get_user(user_id)
        flyers = await cls.flyers_service.get_flyers(user.phone)
        return flyers


flyers_repository = FlyersRepository()
