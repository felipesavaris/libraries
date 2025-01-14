# from pydantic import BaseModel


# # este modelo seria seguindo uma linha de raciocinio usando pydantic
# class Base(BaseModel): ...


# class User(Base):
#     name: str


# class Item(Base):
#     title: str 
#     description: str
#     autor: str
#     genre: str


# class Libary(Base): ...

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry


table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(init=False, onupdate=True)


class Item:
    title: str 
    description: str
    autor: str
    genre: str


class Libary: ...
