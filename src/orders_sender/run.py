from src.orders_sender.consumer import OrdersConsumer


async def run_orders_sender() -> None:
    orders_consumer = OrdersConsumer()
    await orders_consumer.consume_orders()
