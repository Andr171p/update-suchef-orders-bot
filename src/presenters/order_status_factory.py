import os

from typing import Literal

from aiogram.types import FSInputFile
from aiogram.types import InputFile, InlineKeyboardMarkup

from src.config import BASE_DIR
from src.core.entities import Order
from src.misc.file_readers import read_txt


ORDER_STATUSES = Literal[
    "Новый",
    "Принят оператором",
    "Передан на кухню",
    "Готовится",
    "Приготовлен",
    "Укомплектован",
    "Готов для выдачи",
    "Передан курьеру",
    "Доставлен",
    "Завершен успешно",
    "Отменен"
]

PAY_STATUSES = Literal[
    "NEW",
    "CONFIRMED"
]

STATUSES_TEMPLATES_DIR = BASE_DIR / "statuses" / "templates"

STATUSES_PHOTOS_DIR = BASE_DIR / "statuses" / "photos"


class OrderStatusFactory:
    def __init__(self, order: Order) -> None:
        self.order = order

    def get_photo(self) -> "InputFile":
        file_path = os.path.join(STATUSES_PHOTOS_DIR, f"{self.order.status}.png")
        return FSInputFile(file_path)

    def get_text(self) -> str:
        if self.order.status == "Принят оператором":
            file_path = os.path.join(
                STATUSES_TEMPLATES_DIR,
                f"{self.order.status}",
                f"{self.order.delivery_method}.txt"
            )
        else:
            file_path = os.path.join(STATUSES_TEMPLATES_DIR, f"{self.order.status}.txt")
        text = read_txt(file_path)
        return text.format(**self.order.model_dump())

    def get_keyboard(self) -> "InlineKeyboardMarkup":
        if self.order.pay_status != "CONFIRMED":
            return ...
        return ...
