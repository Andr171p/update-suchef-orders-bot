from typing import Literal

from pydantic import BaseModel


class BonusData(BaseModel):
    command: Literal["bonus"] = "bonus"
    telefon: str
    project: Literal["Сушеф.рф"] = "Сушеф.рф"
