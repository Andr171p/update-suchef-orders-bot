from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.repository.flyers import flyers_repository
from src.message.bonus import FlyersMessage


flyers_router = Router()


# @flyers_router.message(F.text == "Мои фишки")
@flyers_router.message(Command("flyers"))
async def get_flyers(message: Message) -> None:
    user_id: int = message.from_user.id
    flyers = await flyers_repository.get_flyers(user_id)
    flyers_message = FlyersMessage(flyers)
    msg = flyers_message.get_message()
    await message.answer_photo(
        photo=msg.photo,
        caption=msg.text,
        reply_markup=msg.keyboard
    )
