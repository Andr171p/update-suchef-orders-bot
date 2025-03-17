from datetime import datetime

from pydantic import BaseModel


class DialogSchema(BaseModel):
    user_id: int
    user_message: str
    bot_message: str
    created_at: datetime
