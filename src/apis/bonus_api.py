from src.apis.base import BaseAPI
from src.http import HTTPClient, JsonResponse
from src.schemas import BonusSchema
from src.apis.schemas import BonusData
from src.misc.validators import is_valid_phone
from src.config import settings


class BonusAPI(BaseAPI):
    _url = settings.api.url
    _headers = settings.api.headers

    async def get_by_phone(self, phone: str) -> BonusSchema | None:
        if not is_valid_phone(phone):
            raise ValueError("Phone number must be in valid format")
        async with HTTPClient(JsonResponse()) as http_client:
            response = await http_client.post(
                url=self._url,
                data=BonusData(telefon=phone).model_dump(),
                headers=self._headers
            )
        return BonusSchema(**response["data"])
