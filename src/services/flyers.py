from typing import Dict

from src.http.client import HTTPClient
from src.schemas.bonus import FlyersSchema
from src.misc.validators import is_valid_phone
from src.misc.formatters import format_phone

from src.config import settings


class FlyersService:
    _url: str = settings.api.url
    _headers: Dict[str, str] = settings.api.headers

    def __init__(self, http_client: HTTPClient) -> None:
        self._http_client = http_client

    async def get_flyers(self, phone: str) -> FlyersSchema:
        if is_valid_phone(phone):
            phone = format_phone(phone)
        json = {
            'command': settings.api.cmd.bonus,
            'telefon': phone,
            'project': settings.project.name
        }
        flyers = await self._http_client.post(
            url=self._url,
            json=json,
            headers=self._headers
        )
        return FlyersSchema(**flyers["data"])
