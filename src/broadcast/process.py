from typing import List, Dict
from aio_pika.abc import AbstractIncomingMessage

from src.app.schemas.order import OrderSchema
from src.broadcast.logger import logger
from src.database.services.service import user_service
from src.broadcast.send import send_order_status


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        body: str = message.body.decode()
        headers: Dict[str, str] = message.headers
        if headers['project'] != "Дисконт Суши":
            logger.info(f"[x] Received: [{body}]")
            order = OrderSchema.parse_raw(body)
            phones: List[str] = order.phones
            for phone in phones:
                user = await user_service.get_user(phone)
                if user is not None:
                    user_id: int = user.user_id
                try:
                    await send_order_status(
                        user_id=user_id,
                        order=order
                    )
                    logger.info(f"message sent to user_id=[{user_id}] successfully")
                except Exception as _ex:
                    logger.warning(_ex)
                    logger.warning(f"message was not sent")
                # finally:
                # await message.ack()
