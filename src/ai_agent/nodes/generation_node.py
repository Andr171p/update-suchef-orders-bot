from langchain_core.runnables import Runnable
from langchain.prompts import ChatPromptTemplate
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser

from src.ai_agent.nodes.base_node import BaseNode
from src.ai_agent.state import State

from src.config import BASE_DIR
from src.misc.file_readers import read_txt


TEMPLATE_PATH = BASE_DIR / "prompts" / "generation_prompt"


class GenerationNode(BaseNode):
    def __init__(self, model: BaseChatModel) -> None:
        self._model = model

    def _create_chain(self) -> Runnable:
        prompt = ChatPromptTemplate.from_template(read_txt(TEMPLATE_PATH))
        return prompt | self._model | StrOutputParser()

    async def execute(self, state: State) -> dict:
        print("---GENERATE---")
        chain = self._create_chain()
        question = state["question"]
        context = state["context"]
        generation = await chain.ainvoke({"context": context, "question": question})
        return {"context": context, "generation": generation, "question": question}
