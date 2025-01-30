from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.database.interfaces import BaseCRUD

    from pydantic import BaseModel

from abc import ABC, abstractmethod


class BaseRepository(ABC):
    _crud: "BaseCRUD"

    @abstractmethod
    async def add(self, model: "BaseModel") -> "BaseModel":
        raise NotImplemented

    @abstractmethod
    async def get_all(self) -> List["BaseModel"]:
        raise NotImplemented
