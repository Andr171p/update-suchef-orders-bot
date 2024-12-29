from pydantic import BaseModel, field_validator

from src.utils.validator import is_valid_phone
from src.utils.format import format_phone


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    phone: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, phone: str) -> str:
        if is_valid_phone(phone):
            phone = format_phone(phone)
        return phone
