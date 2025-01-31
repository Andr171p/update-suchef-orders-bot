from typing import List

from src.apis.base import BaseAPI
from src.apis.schemas import OrdersRequestData
from src.schemas import OrderSchema
from src.http import HTTPClient, JsonResponse
from src.config import settings


class OrderAPI(BaseAPI):
    _url = settings.api.url
    _headers = settings.api.headers

    async def get_orders_by_phone(self, phone: str) -> List[OrderSchema]:
        async with HTTPClient(JsonResponse()) as http_client:
            response = await http_client.post(
                url=self._url,
                data=OrdersRequestData(telefon=phone).model_dump(),
                headers=self._headers
            )
        orders = response["data"]["orders"]
        return [OrderSchema(**order) for order in orders]
