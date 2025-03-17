from aiogram import F, Router
from aiogram.types import Message

from src.config import settings
from src.utils.files import load_json_async
from src.app.keyboards import menu_kb
from src.repository.user_repository import user_repository


register_router = Router()


@register_router.message(F.contact)
async def register_user(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    # log.info(f"User: {user_id} shared contact")
    _ = await user_repository.add_user(user_id, username, phone)
    text = await load_json_async(settings.static.auth)
    await message.answer(
        text=text['success'],
        # reply_markup=menu_kb()
    )
