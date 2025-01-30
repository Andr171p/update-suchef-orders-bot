from src.http.client import HTTPClient
from src.http.responses import JsonResponse


class BonusAPI:
    http_client = HTTPClient(JsonResponse())

