from aiogram import F, Router
from aiogram.types import Message

from src.app.keyboards.promos import promo_page_kb

from src.repository.promo import promo_repository


promos_router = Router()


@promos_router.message(F.text == "Акции")
async def get_promos(message: Message) -> None:
    promos = await promo_repository.get_promos()
    for promo in promos:
        await message.answer_photo(
            photo=promo.url,
            reply_markup=promo_page_kb(promo.title)
        )
