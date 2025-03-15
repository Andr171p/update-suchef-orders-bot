from typing import Optional
from typing_extensions import TypedDict


class GraphState(TypedDict):
    user_id: int
    question: str
    generation: str
    context: str
    is_ok: Optional[bool]
