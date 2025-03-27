from src.rabbit_mq import RabbitConsumer
from src.services.order_status_notifications.rabbit_mq_utils import process_incoming_message


class OrderStatusNotificationsService:
    def __init__(self) -> None:
        ...

    async def callback(self) -> None:
        ...

    async def notify(self) -> ...:
        ...
