from aio_pika.abc import AbstractIncomingMessage

from src.rabbit_mq import RabbitConsumer

from src.orders_sender.processor import OrdersProcessor
from src.orders_sender.sender import OrderSender
from src.app.bot import bot

from src.config import settings


class OrdersConsumer:
    orders_sender = OrderSender(bot)

    @classmethod
    async def _orders_callback(cls, message: AbstractIncomingMessage) -> None:
        async with message.process():
            orders_processor = OrdersProcessor(message)
            order = orders_processor.process_order()
            await cls.orders_sender.send_order(order)

    @classmethod
    async def consume_orders(cls) -> None:
        async with RabbitConsumer() as consumer:
            await consumer.consume_massage(
                message_callback=cls._orders_callback,
                queue_name=settings.rabbit.project_queue_name
            )
