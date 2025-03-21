from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import settings
from src.utils.files import load_json_async
from src.app.keyboards.start import start_kb
from src.app.keyboards.menu import menu_kb
from src.repository.user_repository import user_repository


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    if await user_repository.check_user_exists(user_id):
        text = await load_json_async(settings.static.start)
        await message.answer(
            text=text['already_auth'],
            # reply_markup=menu_kb()
        )
    else:
        text = await load_json_async(settings.static.start)
        await message.answer(
            text=text['start'].format(username=username),
            reply_markup=start_kb()
        )
