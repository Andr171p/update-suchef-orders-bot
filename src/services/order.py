import logging
from typing import AsyncGenerator, Any

from src.apis import OrdersAPI
from src.repository import UserRepository
from src.messages import OrderMessage


log = logging.getLogger(__name__)


class OrdersService:
    _orders_api = OrdersAPI()
    _user_repository = UserRepository()

    async def get_message_by_user_id(self, user_id: int) -> AsyncGenerator[OrderMessage, Any]:
        user = await self._user_repository.get_by_user_id(user_id)
        phone: str = user.phone
        orders = await self._orders_api.get_orders_by_phone(phone)
        log.info(
            "Found %s orders from %s user",
            len(orders),
            user_id
        )
        if not orders:
            return
        for order in orders:
            yield OrderMessage(order)
