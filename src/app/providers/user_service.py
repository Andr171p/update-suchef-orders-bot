from dishka import Provider, Scope, provide

from src.services import UserService


class UserServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_service(self) -> UserService:
        return UserService()
