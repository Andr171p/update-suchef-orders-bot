from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from src.config import settings


def promo_page_kb(text: str) -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text=text, url=settings.project.promo)]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
