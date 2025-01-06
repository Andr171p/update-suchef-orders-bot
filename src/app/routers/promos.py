from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.app.keyboards.promos import promo_page_kb
from src.repository.promo import promo_repository


promos_router = Router()


# @promos_router.message(F.text == "Акции")
@promos_router.message(Command("promos"))
async def get_promos(message: Message) -> None:
    promos = await promo_repository.get_promos()
    for promo in promos:
        print(promo.url)
        await message.answer_photo(
            photo=promo.url,
            reply_markup=promo_page_kb(promo.title)
        )
