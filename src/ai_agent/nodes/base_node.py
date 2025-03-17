from abc import ABC, abstractmethod

from src.ai_agent.states import GraphState


class BaseNode(ABC):
    @abstractmethod
    async def execute(self, state: GraphState) -> dict:
        raise NotImplemented

    async def __call__(self, state: GraphState) -> dict:
        return await self.execute(state)
