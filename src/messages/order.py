from pathlib import Path

from aiogram.types import (
    InlineKeyboardMarkup,
    FSInputFile,
    InputFile
)

from src.messages.base import BaseMessage
from src.schemas.order import OrderSchema
from src.app.keyboards import pay_link_kb, confirmed_link_kb
from src.misc.file_loaders import load_txt
from src.config import settings


class OrderMessage(BaseMessage):
    texts_dir: Path = settings.static.texts_dir / "statuses"
    photos_dir: Path = settings.static.photo_dir / "statuses"

    def __init__(self, order: OrderSchema) -> None:
        self._order = order

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        if self._order.pay_status != "CONFIRMED":
            return pay_link_kb(self._order.pay_link)
        return confirmed_link_kb(self._order.pay_link)

    @property
    def text(self) -> str:
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

    @property
    def photo(self) -> InputFile:
        path: Path = self.photos_dir / f"{self._order.status}.png"
        photo = FSInputFile(str(path))
        return photo
