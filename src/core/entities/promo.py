from pydantic import BaseModel


class Promo(BaseModel):
    url: str
    title: str
