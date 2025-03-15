from typing import AsyncGenerator, Any

from src.apis import PromoAPI
from src.messages import PromoMessage


class PromoService:
    _promo_api = PromoAPI()

    async def get_messages(self) -> AsyncGenerator[PromoMessage, Any]:
        promos = await self._promo_api.get_all_promos()
        for promo in promos:
            yield PromoMessage(promo)
