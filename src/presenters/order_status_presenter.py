from aiogram.types import Message

from src.core.entities import Order
from src.presenters.order_status_factory import OrderStatusFactory


class OrderStatusPresenter:
    def __init__(self, message: Message) -> None:
        self.message = message

    async def present(self, order: Order) -> int:
        order_status_factory = OrderStatusFactory(order)
        message = await self.message.answer_photo(
            photo=order_status_factory.get_photo(),
            caption=order_status_factory.get_text(),
            reply_markup=order_status_factory.get_keyboard()
        )
        return message.message_id
