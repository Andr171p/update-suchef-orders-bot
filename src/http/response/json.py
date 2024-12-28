from typing import Dict, Any

from aiohttp import ClientResponse

from src.http.responses.base import BaseResponse
from src.http.responses.utils import ResponseUtils


class JsonResponse(ResponseUtils, BaseResponse):
    async def data(
            self,
            response: ClientResponse
    ) -> Dict[str, Any] | None:
        if self.is_ok(response):
            return
        return await response.json()
