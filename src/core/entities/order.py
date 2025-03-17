from typing import List

from pydantic import BaseModel, field_validator

from src.misc import formatters


class Order(BaseModel):
    client: str
    number: str
    date: str
    status: str
    amount: float
    pay_link: str
    pay_status: str
    cooking_time_from: str
    cooking_time_to: str
    delivery_time_from: str
    delivery_time_to: str
    project: str
    trade_point: str
    trade_point_card: str
    delivery_method: str
    delivery_adress: str
    phones: List[str]

    @field_validator("number")
    @classmethod
    def validate_number(cls, v: str) -> str:
        return formatters.format_number(v)

    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        return formatters.format_date(v)

    @field_validator(
        "cooking_time_from",
        "cooking_time_to",
        "delivery_time_from",
        "delivery_time_to"
    )
    @classmethod
    def validate_time(cls, v: str) -> str:
        return formatters.format_time(v)

    @field_validator("phones")
    @classmethod
    def validate_phones(cls, values: List[str]) -> List[str]:
        phones = []
        for phone in values:
            phone = formatters.format_phone(phone)
            phones.append(phone)
        return phones

    @field_validator("delivery_adress")
    @classmethod
    def validate_adress(cls, value: str) -> str:
        return formatters.format_address(value)
