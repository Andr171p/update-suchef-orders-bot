from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, InputFile


class AbstractMessage(ABC):
    @abstractmethod
    def _get_keyboard(self) -> InlineKeyboardMarkup:
        raise NotImplemented

    @abstractmethod
    def _get_text(self) -> str:
        raise NotImplemented

    @abstractmethod
    def _get_photo(self) -> InputFile:
        raise NotImplemented
