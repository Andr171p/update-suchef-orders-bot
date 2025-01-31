from pydantic import BaseModel

from aiogram.types import InputFile
from aiogram.types.base import MutableTelegramObject


class BaseMessage(BaseModel):
    photo: InputFile | None
    text: str
    keyboard: MutableTelegramObject | None

    class Config:
        arbitrary_types_allowed = True
