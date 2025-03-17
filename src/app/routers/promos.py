from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.services import PromoService


promos_router = Router()


@promos_router.message(Command("promos"))
async def get_promos(
        message: Message,
        promo_service: FromDishka[PromoService]
) -> None:
    async for promo_message in promo_service.get_messages():
        await message.answer_photo(
            photo=promo_message.photo,
            reply_markup=promo_message.keyboard
        )
