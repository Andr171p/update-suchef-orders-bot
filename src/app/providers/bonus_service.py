from dishka import Provider, Scope, provide

from src.services import BonusService


class BonusServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_bonus_service(self) -> BonusService:
        return BonusService()
