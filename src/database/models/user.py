from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from src.database.models.dialog import Dialog

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class User(Base):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime)

    dialogs: Mapped[list["Dialog"]] = relationship(back_populates="user")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(user_id={self.user_id}, username={self.username}, phone={self.phone})"

    def __repr__(self) -> str:
        return str(self)
