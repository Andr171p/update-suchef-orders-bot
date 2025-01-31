from datetime import datetime

from aiogram import F, Router
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka

from src.services import UserService
from src.schemas import UserSchema
from src.misc.file_loaders import load_json_async
from src.config import settings


register_router = Router()


@register_router.message(F.contact)
async def register_user(
        message: Message,
        user_service: FromDishka[UserService]
) -> None:
    user_id: int = message.from_user.id
    username: str = message.from_user.username
    phone: str = message.contact.phone_number
    user = UserSchema(user_id=user_id, username=username, phone=phone, created_at=datetime.now())
    await user_service.register(user)
    text = await load_json_async(settings.static.auth)
    await message.answer(text['success'])
