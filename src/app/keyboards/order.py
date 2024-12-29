from typing import List

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


async def order_status_kb() -> ReplyKeyboardMarkup:
    keyboard_list: List[List[KeyboardButton]] = [
        [KeyboardButton(text="Статус заказа")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Узнать статус заказа"
    )
    return keyboard


def pay_link_kb(url: str) -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = []
    if url:
        keyboard_list.append(
            [InlineKeyboardButton(text="Оплатить", url=url)]
        )
    else:
        keyboard_list.append(
            [InlineKeyboardButton(text="Не оплачен", callback_data="not payment")]
        )
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard


def confirmed_link_kb(url: str) -> InlineKeyboardMarkup:
    keyboard_list: List[List[InlineKeyboardButton]] = []
    if url:
        keyboard_list.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", url=url)]
        )
    else:
        keyboard_list.append(
            [InlineKeyboardButton(text="ОПЛАЧЕН", callback_data="confirmed")]
        )
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard
