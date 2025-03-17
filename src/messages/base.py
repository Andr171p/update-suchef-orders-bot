from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, InputFile


class BaseMessage(ABC):
    @property
    @abstractmethod
    def keyboard(self) -> InlineKeyboardMarkup:
        raise NotImplemented

    @property
    @abstractmethod
    def text(self) -> str:
        raise NotImplemented

    @property
    @abstractmethod
    def photo(self) -> InputFile | str:
        raise NotImplemented
