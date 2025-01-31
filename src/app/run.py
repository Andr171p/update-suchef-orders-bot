from src.app.bot import bot, dp
from src.app.commands.menu import set_commands


async def run_bot() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    await set_commands(bot)
