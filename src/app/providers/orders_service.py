from dishka import Provider, Scope, provide

from src.services import OrdersService


class OrdersServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_orders_service(self) -> OrdersService:
        return OrdersService()
