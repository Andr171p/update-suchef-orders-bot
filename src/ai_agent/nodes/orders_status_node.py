from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.prompts import BasePromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.output_parsers import BaseTransformOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.states import GraphState

from src.core.use_cases import OrderStatusUseCase
from src.presenters import OrderStatusFactory


class OrderStatusNode(BaseNode):
    def __init__(self, order_status_use_case: OrderStatusUseCase) -> None:
        self._order_status_use_case = order_status_use_case

    async def execute(self, state: GraphState) -> dict:
        print("---RECEIVING ORDER STATUS---")
        user_id = state["user_id"]
        orders = await self._order_status_use_case.get_by_user_id(user_id)
        generation = OrderStatusFactory(orders[0]).get_text()
        return {"generation": generation}
