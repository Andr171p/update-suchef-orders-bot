import logging
from typing import AsyncGenerator, Awaitable, Any, Callable

from src.apis import OrdersAPI
from src.repository import UserRepository
from src.messages import OrderMessage
from src.schemas import OrderSchema


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

    async def send_message(
            self,
            order: OrderSchema,
            on_message: Callable[[int, OrderMessage], Awaitable[None]]
    ) -> None:
        for phone in order.phones:
            user = await self._user_repository.get_by_phone(phone)
            if user is not None:
                await on_message(user.user_id, OrderMessage(order))
