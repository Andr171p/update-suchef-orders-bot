from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.models.user_model import UserModel

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declared_attr,
    relationship
)


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.user_id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable
        )

    @declared_attr
    def user(cls) -> Mapped["UserModel"]:
        return relationship(
            argument="UserModel",
            back_populates=cls._user_back_populates
        )
