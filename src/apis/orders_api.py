from typing import List, Union

from src.http import HTTPClient
from src.http.responses import JsonResponse
from src.core.entities import Order
from src.dto import OrdersDTO


class OrdersAPI:
    def __init__(self, url: str) -> None:
        self._url = url

    async def get_by_phone_number(self, phone_number: str) -> List[Union[Order, None]]:
        async with HTTPClient(JsonResponse()) as http_client:
            response = await http_client.post(
                url=self._url,
                json={
                    "command": "status",
                    "telefon": phone_number
                },
                headers={"Content-Type": "application/json; charset=UTF-8"}
            )
        return OrdersDTO.from_response(response)
