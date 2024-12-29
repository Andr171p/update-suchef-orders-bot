from typing import List

from src.http.client import HTTPClient
from src.http.response import JsonResponse

from src.database.service.user import UserService

from src.service.order import OrderService
from src.schemas.order import OrderSchema

from src.config import settings


class OrderRepository:
    http_client = HTTPClient(JsonResponse())
    order_service = OrderService(http_client)
    user_service = UserService()

    @classmethod
    async def get_user_orders(cls, user_id: int) -> List[OrderSchema] | None:
        user = await cls.user_service.get_user(user_id)
        orders = await cls.order_service.get_orders(user.phone)
        if orders:
            return [
                order
                for order in orders
                if order.project == settings.project.name
            ]


order_repository = OrderRepository()
