from src.core.entities import UserMessage


class ChatBotUseCase:
    async def answer(self, user_message: UserMessage) -> str:
        ...
