from dataclasses import dataclass
from typing import Any, Dict
from aiogram.types import InlineKeyboardMarkup

from src.app.schemas.order import OrderSchema
from src.app.keyboards import order_status
from src.message.message import BotMessage
from src.config import settings
from src import utils


@dataclass
class OrderStatus:
    order: OrderSchema

    async def _get_keyboard(self) -> InlineKeyboardMarkup:
        if self.order.pay_status != "CONFIRMED":
            return await order_status.pay_link_kb(url=self.order.pay_link)
        return await order_status.confirmed_link_kb(url=self.order.pay_link)

    async def _get_text(self) -> str:
        templates: Dict[str, Any] = await utils.load_json(path=settings.msg.statuses)
        if self.order.status == "Принят оператором":
            text: str = templates[self.order.status][self.order.delivery_method]
            return text.format(**self.order.model_dump())
        text: str = templates[self.order.status]
        return text.format(**self.order.model_dump())

    async def get_bot_message(self, user_id: int) -> BotMessage:
        bot_message = BotMessage(
            user_id=user_id,
            text=await self._get_text(),
            keyboard=await self._get_keyboard()
        )
        return bot_message
