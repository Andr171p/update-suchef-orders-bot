from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, InputFile


class AbstractMessage(ABC):
    @abstractmethod
    def _get_keyboard(self) -> InlineKeyboardMarkup: pass

    @abstractmethod
    def _get_text(self) -> str: pass

    @abstractmethod
    def _get_photo(self) -> InputFile: pass
