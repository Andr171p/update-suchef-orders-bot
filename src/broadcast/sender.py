import logging

from aiogram import Bot

from src.schemas.order import OrderSchema
from src.message.order import OrderMessage
from src.database.service.user import UserService


log = logging.getLogger(__name__)


class OrdersSender:
    user_service = UserService()

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def send_message(
            self,
            user_id: int,
            order: OrderSchema
    ) -> None:
        order_message = OrderMessage(order)
        message = order_message.get_message()
        try:
            await self.bot.send_photo(
                chat_id=user_id,
                photo=message.photo,
                caption=message.text,
                reply_markup=message.keyboard
            )
            log.info("Message sent successfully to %s", user_id)
        except Exception as _ex:
            log.warning(_ex)
            log.warning("Message was not sent")

    async def send_order(self, order: OrderSchema) -> None:
        phones = order.phones
        for phone in phones:
            user = await self.user_service.get_user(phone)
            if user is not None:
                user_id = user.user_id
                await self.send_message(
                    user_id=user_id,
                    order=order
                )
