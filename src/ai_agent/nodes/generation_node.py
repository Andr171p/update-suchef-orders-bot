from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.states import GraphState


class GenerationNode(BaseNode):
    def __init__(
            self,
            prompt: "BasePromptTemplate",
            model: "BaseChatModel",
            parser: "BaseTransformOutputParser"
    ) -> None:
        self._chain = prompt | model | parser

    def execute(self, state: GraphState) -> dict:
        print("---GENERATE---")
        question = state["question"]
        context = state["context"]
        generation = self._chain.invoke({"context": context, "question": question})
        return {"context": context, "generation": generation, "question": question}
