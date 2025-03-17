from pydantic import BaseModel


class UserMessage(BaseModel):
    user_id: int
    question: str
