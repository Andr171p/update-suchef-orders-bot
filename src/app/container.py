from dishka import make_async_container

from src.app.providers import (
    UserServiceProvider,
    OrdersServiceProvider,
    BonusServiceProvider,
    PromoServiceProvider
)


container = make_async_container(
    UserServiceProvider(),
    OrdersServiceProvider(),
    BonusServiceProvider(),
    PromoServiceProvider()
)
