from aiohttp import ClientResponse

from src.http.response.abc import AbstractResponse
from src.http.response.checker import ResponseChecker


class TextResponse(ResponseChecker, AbstractResponse):
    async def data(
            self,
            response: ClientResponse
    ) -> str | None:
        if not self.is_ok(response):
            return
        return await response.text()
