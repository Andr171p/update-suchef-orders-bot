from typing import List

from bs4 import BeautifulSoup

from src.http.client import HTTPClient
from src.schemas.promo import PromoSchema
from src.config import settings


class PromoService:
    _project_url: str = settings.project.url
    _promo_url: str = settings.project.promo

    def __init__(self, http_client: HTTPClient) -> None:
        self._http_client = http_client

    async def get_promos(self) -> List[PromoSchema]:
        html = await self._http_client.get(url=self._promo_url)
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all(
            name="div",
            attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"}
        )
        return [
            PromoSchema(url=self._project_url + image["data-src"], title=image["title"])
            for div in divs
            if (image := div.find("img"))
        ]


import asyncio
print(asyncio.run(PromoService().get_promos()))