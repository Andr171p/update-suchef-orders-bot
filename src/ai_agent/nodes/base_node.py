from abc import ABC, abstractmethod

from src.ai_agent.states import GraphState


class BaseNode(ABC):
    @abstractmethod
    def execute(self, state: GraphState) -> dict:
        raise NotImplemented

    def __call__(self, state: GraphState) -> dict:
        return self.execute(state)
