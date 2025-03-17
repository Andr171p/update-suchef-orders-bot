from typing import List, Union

from src.core.entities import Order


class OrdersDTO:
    @staticmethod
    def from_response(response: dict) -> List[Union[Order, None]]:
        orders = response["data"]["orders"]
        return [Order(**order) for order in orders]
