from pydantic import BaseModel, ConfigDict

from models.enums import GenderEnum


class ProfilePydantic(BaseModel):
    name: str | None
    surname: str | None
    age: int | None
    gender: GenderEnum
    interests: list | None
    contacts: dict | None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
