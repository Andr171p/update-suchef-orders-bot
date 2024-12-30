from pydantic import BaseModel


class FlyersSchema(BaseModel):
    flyers: int
    chips: int
