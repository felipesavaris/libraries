from datetime import datetime

from pydantic import BaseModel


class BaseDTO(BaseModel): ...


class UserDTO(BaseDTO):
    name: str
    email: str


class UserInDTO(UserDTO):
    password: str


class UserOutDTO(UserDTO):
    created_at: datetime
    updated_at: datetime


class ItemDTO(BaseDTO):
    title: str 
    description: str
    autor: str
    genre: str


class LibaryDTO(BaseDTO): ...
