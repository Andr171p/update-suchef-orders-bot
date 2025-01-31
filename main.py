import logging
import asyncio

from src.app.run import run_orders_bot
from src.notification.run import run_orders_sender


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await asyncio.gather(
        run_orders_bot(),
        run_orders_sender()
    )


if __name__ == "__main__":
    asyncio.run(main())
