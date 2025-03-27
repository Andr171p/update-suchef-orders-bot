import logging

from typing import Union

from aio_pika.abc import AbstractIncomingMessage

from src.core.entities import Order


log = logging.getLogger(__name__)


async def process_incoming_message(
        message: AbstractIncomingMessage,
        project: str = "Сушеф.рф"
) -> Union[Order, None]:
    body: str = message.body.decode()
    headers: dict = message.headers
    if headers["project"] != project:
        return
    log.info("[x] Received messages: %s", body)
    return Order.model_validate(body)


async def message_callback(message: AbstractIncomingMessage) -> None:
    async with message.process():
        ...
