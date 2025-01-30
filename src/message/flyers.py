from pathlib import Path

from aiogram.types import (
    InlineKeyboardMarkup,
    FSInputFile,
    InputFile
)

from src.message.abc import AbstractMessage
from src.message.base import BaseMessage
from src.schemas.bonus import FlyersSchema
from src.misc.file_loaders import load_txt
from src.app.keyboards.flyers import flyers_kb

from src.config import settings


class FlyersMessage(AbstractMessage):
    texts_dir: Path = settings.static.texts_dir / "flyers"
    photos_dir: Path = settings.static.photo_dir / "flyers"

    def __init__(self, flyers: FlyersSchema) -> None:
        self._flyers = flyers

    def _get_keyboard(self) -> InlineKeyboardMarkup:
        return flyers_kb()

    def _get_text(self) -> str:
        if self._flyers.chips > 0:
            path: Path = self.texts_dir / "Есть флаеры.txt"
        else:
            path: Path = self.texts_dir / "Нет фишек.txt"
        text = load_txt(path)
        return text.format(**self._flyers.model_dump())

    def _get_photo(self) -> InputFile:
        path: Path = self.photos_dir / "flyers.png"
        photo = FSInputFile(str(path))
        return photo

    def get_message(self) -> BaseMessage:
        return BaseMessage(
            photo=self._get_photo(),
            text=self._get_text(),
            keyboard=self._get_keyboard()
        )
