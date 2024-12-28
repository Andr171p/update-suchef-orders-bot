import asyncio

from src.http.client import HTTPClient
from src.http.responses.text import TextResponse


# url: str = "https://imp72.ru/catalog/akcii/"
url = "https://imp72.ru/catalog/akcii/"


client = HTTPClient(TextResponse())
print(asyncio.run(client.get(url=url)))