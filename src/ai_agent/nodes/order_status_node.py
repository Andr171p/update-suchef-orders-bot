from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.states import GraphState


class OrderStatusNode(BaseNode):
    def __init__(self) -> None:
        ...

    def execute(self, state: GraphState) -> dict:
        ...