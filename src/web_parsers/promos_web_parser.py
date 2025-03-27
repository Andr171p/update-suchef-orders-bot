from typing import List

from bs4 import BeautifulSoup

from src.http import HTTPClient
from src.http.responses import TextResponse
from src.core.entities import Promo
from src.dto import PromoDTO


class PromosWebParser:
    def __init__(self, url: str) -> None:
        self._url = url

    async def get_all(self) -> List[Promo]:
        async with HTTPClient(TextResponse()) as http_client:
            html = await http_client.get(self._url)
        soup = BeautifulSoup(html, "html.parser")
        blocks = soup.find_all("div", attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"})
        return [PromoDTO.from_image(image) for block in blocks if (image := block.find("img"))]
    