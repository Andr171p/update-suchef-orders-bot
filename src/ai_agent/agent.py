from pprint import pprint

from langgraph.graph import START, StateGraph, END

from src.ai_agent.states import GraphState
from src.ai_agent.nodes import (
    DecisionNode,
    OrderStatusNode,
    RetrieverNode,
    GenerationNode
)


class Agent:
    def __init__(
            self,
            decision: DecisionNode,
            retriever: RetrieverNode,
            generation: GenerationNode,
            order_status: OrderStatusNode
    ) -> None:
        graph = StateGraph(GraphState)
        """Добавление узлов в граф"""
        graph.add_node("decision", decision)
        graph.add_node("retrieve", retriever)
        graph.add_node("generate", generation)
        graph.add_node("order_status", order_status)
        """Добавление вершин в граф"""
        graph.add_edge(START, "decision")
        graph.add_conditional_edges("decision", lambda x: x["action"])
        graph.add_edge("retrieve", "generate")
        graph.add_edge("generate", END)
        graph.add_edge("order_status", END)
        self._graph_compiled = graph.compile()

    def generate(self, query: str) -> str:
        for output in self._graph_compiled.stream({"question": query}):
            for key, value in output.items():
                pprint(f"Node '{key}':")
            pprint("\n---\n")
        pprint(value["generation"])
        return value["generation"]
