from pydantic import BaseModel


class PromoSchema(BaseModel):
    url: str
    title: str
