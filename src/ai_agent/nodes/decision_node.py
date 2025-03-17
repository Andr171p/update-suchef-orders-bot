from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.states import GraphState


NEXT_STEPS = Literal[
    "retrieve",
    "order_status"
]


class DecisionNode(BaseNode):
    def __init__(
            self,
            prompt: "BasePromptTemplate",
            model: "BaseChatModel",
            parser: "BaseTransformOutputParser"
    ) -> None:
        self._chain = prompt | model | parser

    @staticmethod
    def _get_action_from_response(response: str) -> NEXT_STEPS:
        return "retrieve" if "retrieve" in response else "order_status"

    async def execute(self, state: GraphState) -> dict:
        print("---DECISION MAKING---")
        question = state["question"]
        response = await self._chain.invoke({"question": question})
        action = self._get_action_from_response(response)
        return {"question": question, "action": action}
