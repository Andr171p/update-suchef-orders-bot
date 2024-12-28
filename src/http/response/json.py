from typing import Dict, Any

from aiohttp import ClientResponse

from src.http.response.base import BaseResponse
from src.http.response.utils import ResponseUtils


class JsonResponse(ResponseUtils, BaseResponse):
    async def data(
            self,
            response: ClientResponse
    ) -> Dict[str, Any] | None:
        if self.is_ok(response):
            return
        return await response.json()
