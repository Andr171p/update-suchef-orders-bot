from pathlib import Path

from aiogram.types import (
    InlineKeyboardMarkup,
    FSInputFile,
    InputFile
)

from src.message.base import BaseMessage
from src.schemas import BonusSchema
from src.misc.file_loaders import load_txt
from src.app.keyboards.flyers import flyers_kb
from src.config import settings


class BonusMessage(BaseMessage):
    texts_dir: Path = settings.static.texts_dir / "flyers"
    photos_dir: Path = settings.static.photo_dir / "flyers"

    def __init__(self, bonus: BonusSchema) -> None:
        self._bonus = bonus

    @property
    def keyboard(self) -> InlineKeyboardMarkup:
        return flyers_kb()

    @property
    def text(self) -> str:
        if self._bonus.chips > 0:
            path: Path = self.texts_dir / "Есть флаеры.txt"
        else:
            path: Path = self.texts_dir / "Нет фишек.txt"
        text = load_txt(path)
        return text.format(**self._bonus.model_dump())

    @property
    def photo(self) -> InputFile:
        path: Path = self.photos_dir / "flyers.png"
        photo = FSInputFile(str(path))
        return photo


async def main() -> None:
    from src.apis import BonusAPI
    bonus_api = BonusAPI()
    bonus = await bonus_api.get_by_phone("89199350914")
    message = BonusMessage(bonus)
    print(message.text)


import asyncio
asyncio.run(main())
