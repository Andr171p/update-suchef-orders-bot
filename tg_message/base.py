from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from aiogram.types.base import MutableTelegramObject


class BaseMessage(BaseModel):
    photo: Optional[str | Path]
    text: str
    keyboard: MutableTelegramObject | None
