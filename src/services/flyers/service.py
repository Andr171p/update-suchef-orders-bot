from typing import Dict, Any

from src.http.client import HTTPClient
from src.http.response.json import JsonResponse

from src.config import settings


class FlyersService:
    def __init__(
            self,
            url: str = settings.api.url,
            headers: Dict[str, Any] = settings.api.headers
    ) -> None:
        self._url = url
        self._headers = headers

    async def get_flyers(self, phone: str) -> ...:
        http_client = HTTPClient(JsonResponse())
        json = {
            'command': settings.api.bonus,
            'telefon': phone,
            'project': settings.project.name
        }
        response = await http_client.post(
            url=self._url,
            json=json,
            headers=self._headers
        )
        return response


import asyncio
print(asyncio.run(FlyersService().get_flyers("89199350914")))
