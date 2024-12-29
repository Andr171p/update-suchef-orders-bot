from aiogram import F, Router
from aiogram.types import Message
from typing import Any, Dict, List

from src.services.promos.service import PromoService
from src.app.keyboards.promos import promo_page_kb


promos_router = Router()


@promos_router.message(F.text == "Акции")
async def get_promos(message: Message) -> None:
    promo_service = PromoService()
    promos = await promo_service.get_promos()
    for promo in promos:
        await message.answer_photo(
            photo=promo.url,
            reply_markup=promo_page_kb(text=promo.title)
        )
