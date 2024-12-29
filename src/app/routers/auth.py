import logging

from aiogram import F, Router
from aiogram.types import Message

from src.config import settings
from src.utils.files import load_json_async
from src.app.keyboards import menu_kb
from src.repository.auth import auth_repository


log = logging.getLogger(__name__)

auth_router = Router()


@auth_router.message(F.contact)
async def register_user(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    log.info(f"User: {user_id} shared contact")
    _ = await auth_repository.register_user(user_id, username, phone)
    text = await load_json_async(settings.msg.auth)
    await message.answer(
        text=text['success'],
        reply_markup=menu_kb()
    )
