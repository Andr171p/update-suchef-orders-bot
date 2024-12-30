from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from src.config import settings


def flyers_kb() -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="Перейти на сайт", url=settings.project.url)]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
