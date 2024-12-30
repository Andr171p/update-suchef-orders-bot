from typing import List, Dict

from src.http.client import HTTPClient
from src.schemas.order import OrderSchema
from src.utils.validator import is_valid_phone
from src.utils.format import format_phone

from src.config import settings


class OrderService:
    _url: str = settings.api.url
    _headers: Dict[str, str] = settings.api.headers

    def __init__(self, http_client: HTTPClient) -> None:
        self._http_client = http_client

    async def get_orders(self, phone: str) -> List[OrderSchema]:
        if is_valid_phone(phone):
            phone = format_phone(phone)
        print(phone)
        print(settings.api.cmd.status)
        print(type(settings.api.cmd.status))
        json = {
            "command": settings.api.cmd.status,
            "telefon": phone
        }
        orders = await self._http_client.post(
            url=self._url,
            json=json,
            headers=self._headers
        )
        return [
            OrderSchema(**order)
            for order in orders["data"]["orders"]
        ]
