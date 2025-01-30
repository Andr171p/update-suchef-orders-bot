from datetime import datetime

from sqlalchemy import Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.database.models.mixins import UserRelationMixin


class Dialog(UserRelationMixin, Base):
    _user_back_populates = "dialogs"

    user_message: Mapped[str] = mapped_column(Text)
    bot_message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(user_id={self.user_id}, created_at={self.user_id})"

    def __repr__(self) -> str:
        return str(self)
