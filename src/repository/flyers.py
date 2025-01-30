from src.database.crud.user import UserService
from src.http.client import HTTPClient
from src.http.responses import JsonResponse
from src.services.flyers import FlyersService
from src.schemas import BonusSchema


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
