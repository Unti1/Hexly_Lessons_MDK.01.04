from enum import Enum


class GenderEnum(str, Enum):
    MALE = 'Мужчина'
    FEMALE = 'Женщина'
    UNDEFINED = 'Не выставлен'