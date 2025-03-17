import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram import Bot

from src.messages import OrderMessage


log = logging.getLogger(__name__)


class OrdersSender:
    def __init__(self, bot: "Bot") -> None:
        self._bot = bot

    async def send_message_by_user_id(
            self,
            user_id: int,
            message: OrderMessage
    ) -> None:
        try:
            await self._bot.send_photo(
                chat_id=user_id,
                photo=message.photo,
                caption=message.text,
                reply_markup=message.keyboard
            )
            log.info("Message sent successfully to %s", user_id)
        except Exception as _ex:
            log.warning("Message was not sent due to reason %s", _ex)
