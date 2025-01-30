from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

from src.http.responses.base import BaseResponse


class TextResponse(BaseResponse):
    async def get_data(self, response: "ClientResponse") -> str | None:
        if not self.is_ok(response):
            return
        return await response.text()
