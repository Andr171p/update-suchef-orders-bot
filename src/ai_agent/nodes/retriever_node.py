from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.retrievers import BaseRetriever

from src.ai_agent.states import GraphState
from src.ai_agent.utils import format_docs
from src.ai_agent.nodes.base_node import BaseNode


class RetrieverNode(BaseNode):
    def __init__(self, retriever: "BaseRetriever") -> None:
        self._retriever = retriever

    def execute(self, state: GraphState) -> dict:
        print("---RETRIEVE---")
        question = state["question"]
        documents = self._retriever.get_relevant_documents(question)
        context = format_docs(documents)
        return {"context": context, "question": question}
