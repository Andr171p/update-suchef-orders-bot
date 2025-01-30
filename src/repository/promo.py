from typing import List

from src.http.client import HTTPClient
from src.http.responses import TextResponse

from src.services.promos import PromoService
from src.schemas.promo import PromoSchema


class PromoRepository:
    http_client = HTTPClient(TextResponse())
    promo_service = PromoService(http_client)

    @classmethod
    async def get_promos(cls) -> List[PromoSchema]:
        return await cls.promo_service.get_promos()


promo_repository = PromoRepository()
