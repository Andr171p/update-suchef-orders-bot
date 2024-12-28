from typing import List

from bs4 import BeautifulSoup

from src.http.client import HTTPClient
from src.http.response.text import TextResponse
from src.services.promo.schemas import PromoSchema
from src.config import settings


class PromoService:
    def __init__(
            self,
            base_url: str = settings.product.url,
            promo_page_url: str = settings.product.promo
    ) -> None:
        self._base_url = base_url
        self._promo_page_url = promo_page_url

    async def _fetch_html(self) -> BeautifulSoup:
        http_client = HTTPClient(TextResponse())
        html = await http_client.get(self._promo_page_url)
        return BeautifulSoup(
            markup=html,
            features="html.parser"
        )

    async def get_promos(self) -> List[PromoSchema]:
        soup = await self._fetch_html()
        divs = soup.find_all(
            name="div",
            attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"}
        )
        return [
            PromoSchema(url=self._base_url + image["data-src"], title=image["title"])
            for div in divs
            if (image := div.find("img"))
        ]
