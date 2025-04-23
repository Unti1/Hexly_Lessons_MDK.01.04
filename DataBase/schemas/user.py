import re
from typing import Annotated, Union
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator
from models.enums import GenderEnum
from schemas.profile import ProfilePydantic


class UserPydantic(BaseModel):
    username: str
    email: str
    phone: str | None

    profile: ProfilePydantic | None

    model_config = ConfigDict(from_attributes=True)


class UserReg(BaseModel):
    username: str = Field(
        default=...,
        min_length=3,
        max_length=32,
        description="Имя пользователя, на латинице с использованием цифр",
    )
    password: str = Field(
        default=...,
        min_length=8,
        description="Пароль пользователя, включает обязательно латиницу, хотя одну цифру и знак пунктуации",
    )
    email: EmailStr = Field(default=..., description="Электронная почта пользователя")
    phone: str | None = Field(
        default=None, description="Номер телефона пользователя (Опционально)"
    )

    name: str | None = Field(default=None)
    surname: str | None = Field(None)
    age: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Возраст пользователя, может быть от 0 до 100",
    )
    gender: GenderEnum = Field(
        default=GenderEnum.UNDEFINED, description="Пол пользователя"
    )
    interests: list | None = Field(None)
    contacts: dict | None = Field(None)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str | None) -> str:
        if not value:
            return value

        value = (
            value.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        )
        if not re.match(r"^\+?\d{1,15}$", value):
            raise ValueError(
                'Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр'
            )
        return value

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)


class UserRegV2(BaseModel):
    username: str = Field(
        default=...,
        min_length=3,
        max_length=32,
        description="Имя пользователя, на латинице с использованием цифр",
    )
    password: str = Field(
        default=...,
        min_length=8,
        description="Пароль пользователя, включает обязательно латиницу, хотя одну цифру и знак пунктуации",
    )
    email: EmailStr = Field(default=..., description="Электронная почта пользователя")
    
    phone: Annotated[
        Union[str, PhoneNumber],
        PhoneNumberValidator(),
    ]

    name: str | None = Field(default=None)
    surname: str | None = Field(None)
    age: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Возраст пользователя, может быть от 0 до 100",
    )
    gender: GenderEnum = Field(
        default=GenderEnum.UNDEFINED, description="Пол пользователя"
    )
    interests: list | None = Field(None)
    contacts: dict | None = Field(None)
