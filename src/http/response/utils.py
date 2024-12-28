import logging

from aiohttp import ClientResponse


log = logging.getLogger(__name__)


class ResponseUtils:
    @staticmethod
    def is_ok(response: ClientResponse) -> bool:
        log.info("Response status code: %s", response.status)
        return True if response.status == 200 else False
