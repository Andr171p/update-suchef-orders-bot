import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aio_pika.abc import AbstractIncomingMessage

from src.rabbit_mq import RabbitConsumer
from src.schemas import OrderSchema
from src.services import OrdersService
from src.services.sender import OrdersSender
from src.app.bot import bot
from src.config import settings


log = logging.getLogger(__name__)


def _process_incoming_orders_message(message: "AbstractIncomingMessage") -> OrderSchema | None:
    body: str = message.body.decode()
    headers: dict = message.headers
    if headers["project"] != settings.project.name:
        return
    log.info("[x] Received messages: %s", body)
    return OrderSchema.parse_raw(body)


async def _orders_message_callback(message: "AbstractIncomingMessage") -> None:
    service = OrdersService()
    sender = OrdersSender(bot)
    async with message.process():
        order = _process_incoming_orders_message(message)
        await service.send_message(order, sender.send_message_by_user_id)


async def notify_users_with_orders_messages() -> None:
    async with RabbitConsumer() as consumer:
        await consumer.consume_massage(
            message_callback=_orders_message_callback,
            queue_name=settings.rabbit.project_queue_name
        )
