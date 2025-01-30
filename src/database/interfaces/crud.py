from typing import Sequence
from abc import ABC, abstractmethod

from src.database.base import ModelType


class BaseCRUD(ABC):
    @abstractmethod
    async def create(self, model: ModelType) -> ModelType:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> Sequence[ModelType]:
        raise NotImplemented
