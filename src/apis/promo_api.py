from typing import List

from bs4 import BeautifulSoup

from src.apis.base import BaseAPI
from src.http import HTTPClient, TextResponse
from src.schemas import PromoSchema
from src.config import settings


class PromoAPI(BaseAPI):
    _url = settings.project.promo
    _project_url = settings.project.url

    async def get_all_promos(self) -> List[PromoSchema]:
        async with HTTPClient(TextResponse()) as http_client:
            markup = await http_client.get(self._url)
        soup = BeautifulSoup(markup, "html.parser")
        blocks = soup.find_all(
            name="div",
            attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"}
        )
        return [
            PromoSchema(url=self._project_url + image["data-src"], title=image["title"])
            for block in blocks
            if (image := block.find("img"))
        ]
