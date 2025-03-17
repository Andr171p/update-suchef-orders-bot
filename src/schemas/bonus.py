from pydantic import BaseModel


class BonusSchema(BaseModel):
    flyers: int
    chips: int
