from typing import List

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def menu_kb() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]] = [
        [KeyboardButton(text="Статус заказа")],
        [KeyboardButton(text="Акции")],
        [KeyboardButton(text="Мои фишки")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Узнать статус заказа"
    )
    return keyboard
