from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from aiogram import Bot
    from aiogram.types import InputFile, InlineKeyboardMarkup

import logging

from src.services.sender.base_sender_service import BaseSenderService
from src.services.sender.exceptions import SenderException


log = logging.getLogger(__name__)


class TelegramSenderService(BaseSenderService):
    def __init__(self, bot: "Bot") -> None:
        self._bot = bot

    async def send_message(
            self,
            user_id: int,
            text: str,
            keyboard: Optional["InlineKeyboardMarkup"]
    ) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_message(
                chat_id=user_id,
                text=text,
                reply_markup=keyboard
            )
            if message:
                is_delivered = True
                log.info("Message delivered successfully to %s", user_id)
        except SenderException as se:
            log.warning("Message is not delivered with exception %s", se)
            is_delivered = False
        finally:
            return is_delivered

    async def send_message_with_photo(
            self,
            user_id: int,
            photo: "InputFile",
            text: str,
            keyboard: Optional["InlineKeyboardMarkup"]
    ) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_photo(
                chat_id=user_id,
                photo=photo,
                caption=text,
                reply_markup=keyboard
            )
            if message:
                is_delivered = True
                log.info("Message delivered successfully to %s", user_id)
        except SenderException as se:
            log.warning("Message is not delivered with exception %s", se)
            is_delivered = False
        finally:
            return is_delivered
