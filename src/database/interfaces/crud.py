from typing import Sequence, Any
from abc import ABC, abstractmethod

from src.database.base import ModelType


class BaseCRUD(ABC):
    @abstractmethod
    async def create(self, model: ModelType) -> ModelType:
        raise NotImplemented

    @abstractmethod
    async def read_by_user_id(self, user_id: int) -> Any:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> Sequence[ModelType]:
        raise NotImplemented
