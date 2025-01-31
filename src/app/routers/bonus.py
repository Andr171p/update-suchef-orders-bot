from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.services import BonusService


bonus_router = Router()


@bonus_router.message(Command("flyers"))
async def get_bonus(
        message: Message,
        bonus_service: FromDishka[BonusService]
) -> None:
    user_id: int = message.from_user.id
    bonus_message = await bonus_service.get_message_by_user_id(user_id)
    await message.answer_photo(
        photo=bonus_message.photo,
        caption=bonus_message.text,
        reply_markup=bonus_message.keyboard
    )
