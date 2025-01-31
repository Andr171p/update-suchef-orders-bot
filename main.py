import logging
import asyncio

from src.app.run import run_bot
from src.utils.notification import notify_users_with_orders_messages


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await asyncio.gather(
        run_bot(),
        notify_users_with_orders_messages()
    )


if __name__ == "__main__":
    asyncio.run(main())
