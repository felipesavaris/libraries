from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel): ...


class User(Base):
    name: str
    email: str


class UserIn(User):
    password: str


class UserOut(User):
    created_at: datetime
    updated_at: datetime


class Item(Base):
    title: str 
    description: str
    autor: str
    genre: str


class Libary(Base): ...
