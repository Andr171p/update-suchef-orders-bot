from pprint import pprint
from typing import Optional

from langgraph.graph import START, StateGraph, END

from src.ai_agent.states import GraphState
from src.ai_agent.nodes import (
    RewriterNode,
    RetrieverNode,
    GenerationNode,
    CheckerNode
)


class Agent:
    def __init__(
            self,
            rewriter: RewriterNode,
            retriever: RetrieverNode,
            generation: GenerationNode,
            checker: CheckerNode
    ) -> None:
        workflow = StateGraph(GraphState)
        """Добавление узлов в граф"""
        workflow.add_node("rewrite", rewriter)
        workflow.add_node("retrieve", retriever)
        workflow.add_node("generate", generation)
        workflow.add_node("check", checker)
        """Добавление вершин в граф"""
        workflow.add_edge(START, "rewrite")
        workflow.add_edge("rewrite", "retrieve")
        workflow.add_edge("retrieve", "generate")
        workflow.add_edge("generate", "check")
        workflow.add_conditional_edges("check", self.decide_to_repeat)
        workflow.add_edge("generate", END)
        self._compiled_workflow = workflow.compile()

    @staticmethod
    def decide_to_repeat(state: GraphState) -> str:
        is_ok: Optional[bool] = state.get("is_ok")
        return END if not is_ok else "rewrite"

    def generate(self, query: str) -> str:
        for output in self._compiled_workflow.stream({"question": query}):
            for key, value in output.items():
                pprint(f"Node '{key}':")
            pprint("\n---\n")
        pprint(value["generation"])
        return value["generation"]
