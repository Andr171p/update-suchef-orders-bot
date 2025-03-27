from typing import Any

from src.core.entities import Promo


class PromoDTO:
    @staticmethod
    def from_image(image: Any) -> Promo:
        return Promo(
            url=image["data-src"],
            title=image["title"]
        )
