import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.repository.order import order_repository
from src.message.order import OrderMessage
from src.misc.file_loaders import load_json_async
from src.app.keyboards.menu import menu_kb

from src.config import settings


log = logging.getLogger(__name__)

order_router = Router()


# @order_router.message(F.text == "Статус заказа")
@order_router.message(Command("orders"))
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    orders = await order_repository.get_user_orders(user_id)
    if orders:
        for order in orders:
            order_message = OrderMessage(order)
            msg = order_message.get_message()
            await message.answer_photo(
                photo=msg.photo,
                caption=msg.text,
                reply_markup=msg.keyboard
            )
            log.info("Sent order to user %s", user_id)
            log.info(order)
    else:
        template = await load_json_async(settings.static.exc)
        await message.answer(
            text=template["empty"],
            # reply_markup=menu_kb()
        )
