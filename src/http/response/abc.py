from typing import Union, Dict, Any
from abc import ABC, abstractmethod

from aiohttp import ClientResponse


class AbstractResponse(ABC):
    @abstractmethod
    def is_ok(
            self,
            response: ClientResponse
    ) -> bool: pass

    @abstractmethod
    async def data(
            self,
            response: ClientResponse
    ) -> Union[Dict[str, Any]] | None: pass
