from aiogram.types import InlineKeyboardMarkup

from src.messages.base import BaseMessage
from src.schemas import PromoSchema
from src.app.keyboards.promos import promo_page_kb


class PromoMessage(BaseMessage):
    def __init__(self, promo: PromoSchema) -> None:
        self._promo = promo

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        return promo_page_kb(self._promo.title)

    @property
    def text(self) -> str:
        """Нужно будет переделать интерфейс, а то херня какая-то"""
        raise NotImplemented

    @property
    def photo(self) -> str:
        return self._promo.url
