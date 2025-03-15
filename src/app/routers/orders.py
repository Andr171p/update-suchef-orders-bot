from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.services import OrdersService
from src.misc.file_loaders import load_json_async
from src.config import settings


orders_router = Router()


@orders_router.message(Command("orders"))
async def get_orders(
        message: Message,
        orders_service: FromDishka[OrdersService]
) -> None:
    user_id: int = message.from_user.id
    orders_messages = orders_service.get_messages_by_user_id(user_id)
    if orders_messages is None:
        template = await load_json_async(settings.static.exc)
        await message.answer(template["empty"])
    else:
        async for order_message in orders_messages:
            await message.answer_photo(
                photo=order_message.photo,
                caption=order_message.text,
                reply_markup=order_message.keyboard
            )
