from dishka import Provider, Scope, provide

from src.services import PromoService


class PromoServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_promo_service(self) -> PromoService:
        return PromoService()
