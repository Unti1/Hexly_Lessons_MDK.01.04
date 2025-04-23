from typing import List

from sqlalchemy import ARRAY, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.enums import GenderEnum
from settings.database import Base


class Profile(Base):
    name: Mapped[str | None]
    surname: Mapped[str | None]
    age: Mapped[int | None]
    gender: Mapped[GenderEnum] = mapped_column(
        default=GenderEnum.UNDEFINED, server_default=text("'UNDEFINED'")
    )
    interests: Mapped[List[str] | None] = mapped_column(ARRAY(String))
    contacts: Mapped[dict | None] = mapped_column(JSON)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="profile", uselist=False)
