from typing import Optional, Dict, Any

from aiohttp import ClientSession

from src.http.response.abc import AbstractResponse
from src.http.abc import AbstractClient


class HTTPClient(AbstractClient):
    def __init__(self, response_type: AbstractResponse) -> None:
        self._response_type = response_type

    async def get(
            self,
            url: str,
            headers: Optional[Dict[str, Any]] = None
    ) -> Any:
        async with ClientSession() as session:
            async with session.get(
                url=url,
                headers=headers
            ) as response:
                return await self._response_type.data(response)

    async def post(
            self,
            url: str,
            json: Dict[str, Any],
            headers: Optional[Dict[str, Any]] = None
    ) -> Any:
        async with ClientSession() as session:
            async with session.post(
                url=url,
                headers=headers,
                json=json
            ) as response:
                return await self._response_type.data(response)
