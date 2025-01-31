from typing import Literal

from pydantic import BaseModel


class BonusRequestData(BaseModel):
    command: Literal["bonus"] = "bonus"
    telefon: str
    project: Literal["Сушеф.рф"] = "Сушеф.рф"


class OrdersRequestData(BaseModel):
    command: Literal["status"] = "status"
    telefon: str
