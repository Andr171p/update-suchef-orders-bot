from pathlib import Path

from aiogram.types import InlineKeyboardMarkup, InputFile

from src.schemas.order import OrderSchema
from src.app.keyboards import pay_link_kb, confirmed_link_kb

from src.message.base import BaseMessage

from src.utils.files import load_txt
from src.config import settings


class OrderMessage:
    texts_dir: Path = settings.static.texts_dir / "statuses"
    photos_dir: Path = settings.static.photo_dir / "statuses"

    def __init__(self, order: OrderSchema) -> None:
        self._order = order

    def _get_keyboard(self) -> InlineKeyboardMarkup:
        if self._order.pay_status != "CONFIRMED":
            return pay_link_kb(self._order.pay_link)
        return confirmed_link_kb(self._order.pay_link)

    def _get_text(self) -> str:
        if self._order.status == "Принят оператором":
            path: Path = (
                    self.texts_dir /
                    f"{self._order.status}" /
                    f"{self._order.delivery_method}.txt"
            )
        else:
            path: Path = self.texts_dir / f"{self._order.status}.txt"
        text: str = load_txt(path)
        return text.format(**self._order.model_dump())

    def _get_photo(self) -> InputFile:
        path: Path = self.photos_dir / f"{self._order.status}.png"
        photo = InputFile(str(path))
        return photo

    def get_message(self) -> BaseMessage:
        return BaseMessage(
            photo=self._get_photo(),
            text=self._get_text(),
            keyboard=self._get_keyboard()
        )
