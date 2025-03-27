from langgraph.graph import START, StateGraph, END

from src.ai_agent.state import State
from src.ai_agent.nodes import (
    DecisionNode,
    OrderStatusNode,
    RetrieverNode,
    GenerationNode
)


class Agent:
    def __init__(
            self,
            decision_node: DecisionNode,
            retriever_node: RetrieverNode,
            generation_node: GenerationNode,
            order_status_node: OrderStatusNode
    ) -> None:
        graph = StateGraph(State)

        graph.add_node("decision", decision_node)
        graph.add_node("retrieve", retriever_node)
        graph.add_node("generate", generation_node)
        graph.add_node("order_status", order_status_node)

        graph.add_edge(START, "decision")
        graph.add_conditional_edges("decision", lambda x: x["action"])
        graph.add_edge("retrieve", "generate")
        graph.add_edge("generate", END)
        graph.add_edge("order_status", END)

        self._graph_compiled = graph.compile()

    async def generate(self, query: str) -> str:
        return await self._graph_compiled.ainvoke({"question": query})
