from typing import Dict, Any

from aiohttp import ClientResponse

from src.http.response.abc import AbstractResponse
from src.http.response.checker import ResponseChecker


class JsonResponse(ResponseChecker, AbstractResponse):
    async def data(
            self,
            response: ClientResponse
    ) -> Dict[str, Any] | None:
        if self.is_ok(response):
            return
        return await response.json()
