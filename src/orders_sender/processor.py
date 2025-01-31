import logging

from typing import Dict

from aio_pika.abc import AbstractIncomingMessage

from src.schemas.order import OrderSchema
from src.config import settings


log = logging.getLogger(__name__)


class OrdersProcessor:
    def __init__(self, message: AbstractIncomingMessage) -> None:
        self.message = message

    def process_order(self) -> OrderSchema | None:
        body: str = self.message.body.decode()
        headers: Dict[str, str] = self.message.headers
        if headers["project"] == settings.project.name:
            log.info("[x] Received messages: %s", body)
            order = OrderSchema.parse_raw(body)
            return order
