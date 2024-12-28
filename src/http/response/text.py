from aiohttp import ClientResponse

from src.http.responses.base import BaseResponse
from src.http.responses.utils import ResponseUtils


class TextResponse(ResponseUtils, BaseResponse):
    async def data(
            self,
            response: ClientResponse
    ) -> str | None:
        if not self.is_ok(response):
            return
        return await response.text()
