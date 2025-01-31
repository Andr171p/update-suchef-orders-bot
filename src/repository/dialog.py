from typing import List

from src.repository.base import BaseRepository
from src.database.crud import DialogCRUD
from src.database.models import Dialog
from src.schemas import DialogSchema


class DialogRepository(BaseRepository):
    _crud = DialogCRUD()

    async def add(self, dialog: DialogSchema) -> DialogSchema:
        added_dialog = await self._crud.create(Dialog(**dialog.model_dump()))
        return DialogSchema(**added_dialog.__dict__)

    async def get_by_user_id(self, user_id: int) -> List[DialogSchema] | None:
        dialogs = await self._crud.read_by_user_id(user_id)
        if dialogs is None:
            return
        return [DialogSchema(**dialog.__dict__) for dialog in dialogs]

    async def get_all(self) -> List[DialogSchema]:
        dialogs = await self._crud.read_all()
        return [DialogSchema(**dialog.__dict__) for dialog in dialogs]


import asyncio
async def main() -> None:
    repo = DialogRepository()
    dialogs = await repo.get_by_user_id(123)
    print(dialogs)


asyncio.run(main())
