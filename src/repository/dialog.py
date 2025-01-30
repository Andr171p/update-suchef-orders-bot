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

    async def get_all(self) -> List[DialogSchema]:
        dialogs = await self._crud.read_all()
        return [DialogSchema(**dialog.__dict__) for dialog in dialogs]
