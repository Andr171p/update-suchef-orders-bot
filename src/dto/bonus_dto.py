from src.core.entities import Bonus


class BonusDTO:
    @staticmethod
    def from_response(response: dict) -> Bonus:
        return Bonus(**response["data"])
