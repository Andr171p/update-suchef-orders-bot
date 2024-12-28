import asyncio

from typing import List

from src.http.client import HTTPClient
from src.http.response.text import TextResponse

from bs4 import BeautifulSoup


# url: str = "https://imp72.ru/catalog/akcii/"
url = "https://imp72.ru/catalog/akcii/"

from pydantic import BaseModel

div_class: str = "flex-grid__item flex-grid__item_max-width product-ajax-cont"
class PromoSchema(BaseModel):
    url: str
    title: str


from src.config import settings


class PromoService:
    def __init__(
            self,
            url: str = settings.product.url,
            path: str = settings.product.promo
    ) -> None:
        self._url = url
        self._promo_route = f"{url}{path}"

    @staticmethod
    async def _fetch_html() -> BeautifulSoup:
        http_client = HTTPClient(TextResponse())
        html = await http_client.get(url)
        return BeautifulSoup(
            markup=html,
            features="html.parser"
        )

    async def get_promos(self) -> List[PromoSchema]:
        soup = await self._fetch_html()
        divs = soup.find_all(
            name="div",
            attrs={"class": div_class}
        )
        return [
            PromoSchema(url=self._url + image["data-src"], title=image["title"])
            for div in divs
            if (image := div.find("img"))
        ]


print(asyncio.run(PromoService().get_promos()))
