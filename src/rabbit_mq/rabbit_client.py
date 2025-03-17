from src.rabbit_mq.rabbit_base import RabbitBase
from src.rabbit_mq.rabbit_exchange import RabbitExchange


class RabbitClient(RabbitExchange, RabbitBase):
    pass
