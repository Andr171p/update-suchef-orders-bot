from typing import Dict

from src.http.client import HTTPClient

from src.config import settings


class FlyersService:
    _url: str = settings.api.url
    _headers: Dict[str, str] = settings.api.headers

    def __init__(self, http_client: HTTPClient) -> None:
        self._http_client = http_client

    async def get_flyers(self, phone: str) -> ...:
        json = {
            'command': settings.api.bonus,
            'telefon': phone,
            'project': settings.project.name
        }
        response = await self._http_client.post(
            url=self._url,
            json=json,
            headers=self._headers
        )
        return response
