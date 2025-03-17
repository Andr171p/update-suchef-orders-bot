from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from src.database.crud import BaseCRUD

    from pydantic import BaseModel

from abc import ABC, abstractmethod


class BaseRepository(ABC):
    _crud: "BaseCRUD"

    @abstractmethod
    async def save(self, item: "BaseModel") -> int:
        raise NotImplemented

    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> Union["BaseModel", List["BaseModel"]]:
        raise NotImplemented

    @abstractmethod
    async def get_all(self) -> List["BaseModel"]:
        raise NotImplemented
