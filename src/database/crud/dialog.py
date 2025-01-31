from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.database.manager import DatabaseManager

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.database.interfaces import BaseCRUD
from src.database.provider import get_database_manager
from src.database.models import Dialog


class DialogCRUD(BaseCRUD):
    def __init__(
            self,
            manager: "DatabaseManager" = get_database_manager()
    ) -> None:
        self._manager = manager

    async def create(self, dialog: Dialog) -> Dialog:
        async with self._manager.session() as session:
            session.add(dialog)
            await session.commit()
            await session.refresh(dialog)
        return dialog

    async def read_by_user_id(self, user_id: int) -> Sequence[Dialog]:
        async with self._manager.session() as session:
            stmt = (
                select(Dialog)
                .where(Dialog.user_id == user_id)
                .options(selectinload(Dialog.user))
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()

    async def read_all(self) -> Sequence[Dialog]:
        async with self._manager.session() as session:
            stmt = select(Dialog)
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
