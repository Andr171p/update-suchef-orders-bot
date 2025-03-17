from typing import List

from src.core.entities import Order
from src.repository import UserRepository
from src.apis import OrdersAPI


class OrderStatusUseCase:
    def __init__(
            self,
            orders_api: OrdersAPI,
            user_repository: UserRepository
    ) -> None:
        self._orders_api = orders_api
        self._user_repository = user_repository

    async def get_by_user_id(self, user_id) -> List[Order]:
        phone_number = await self._user_repository.get_phone_number_by_user_id(user_id)
        orders = await self._orders_api.get_by_phone_number(phone_number)
        return orders
