from datetime import datetime

from pydantic import BaseModel, field_validator

from src.misc.validators import is_valid_phone
from src.misc.formatters import format_phone


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    phone: str
    created_at: datetime

    @field_validator("phone")
    @classmethod
    def format_to_current_phone(cls, phone: str) -> str:
        if is_valid_phone(phone):
            phone = format_phone(phone)
        return phone
