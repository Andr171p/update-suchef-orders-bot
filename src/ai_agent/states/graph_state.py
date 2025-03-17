from typing import Literal
from typing_extensions import TypedDict


class GraphState(TypedDict):
    user_id: int
    question: str
    generation: str
    context: str
    action: Literal["retrieve", "order_status"]
