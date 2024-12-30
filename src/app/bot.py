from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from src.app.routers import (
    start_router,
    register_router,
    order_router,
    promos_router,
    flyers_router
)

from src.config import settings


bot: Bot = Bot(
    token=settings.bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp: Dispatcher = Dispatcher(
    storage=MemoryStorage()
)

dp.include_routers(
    start_router,
    register_router,
    order_router,
    promos_router,
    flyers_router
)
