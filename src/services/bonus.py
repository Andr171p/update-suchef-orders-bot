import logging

from src.apis import BonusAPI
from src.repository import UserRepository
from src.messages import BaseMessage, BonusMessage


log = logging.getLogger(__name__)


class BonusService:
    _bonus_api = BonusAPI()
    _user_repository = UserRepository()

    async def get_message_by_user_id(self, user_id: int) -> BaseMessage | None:
        user = await self._user_repository.get_by_user_id(user_id)
        phone: str = user.phone
        bonus = await self._bonus_api.get_by_phone(phone)
        if not bonus:
            return
        log.info(
            "Found chips %s and flyers %s from %s user",
            bonus.chips,
            bonus.flyers,
            user_id
        )
        return BonusMessage(bonus)
