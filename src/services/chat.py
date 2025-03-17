from src.repository import DialogRepository
from src.schemas import DialogSchema


class ChatService:
    _dialog_repository = DialogRepository()

    async def answer_on_question(self, question: str) -> str:
        ...

    async def save_dialog(self, dialog: DialogSchema) -> None:
        ...
