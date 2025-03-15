from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.config import settings
from src.misc.file_loaders import load_json_async
from src.app.keyboards.start import start_kb
from src.services import UserService


start_router = Router()


@start_router.message(Command("start"))
async def start(
        message: Message,
        user_service: FromDishka[UserService]
) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    if await user_service.verify(user_id):
        text = await load_json_async(settings.static.start)
        await message.answer(text['already_auth'])
    else:
        text = await load_json_async(settings.static.start)
        await message.answer(
            text=text['start'].format(username=username),
            reply_markup=start_kb()
        )
