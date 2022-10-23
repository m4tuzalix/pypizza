import sqlalchemy as sa
from pydantic import EmailStr
from SQL.pizza.schemas import OrderedPizza
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlmodel import SQLModel, Field, ARRAY
from datetime import datetime
from typing import List
from enum import Enum, auto


class Status(Enum):
    VERIFICATION = auto()
    ACCEPTED = auto()
    IN_PROGRESS = auto()
    IN_TRANSPORT = auto()
    DELIVERED = auto()


class OrderBase(SQLModel):
    name: str
    surname: str
    email: EmailStr
    phone: str = Field(min_length=9, max_length=9)
    postal_code: str = Field(min_length=6, max_length=6)
    address: str
    active: bool = Field(default=True, include=False)
    pizzas: List[OrderedPizza] = Field(
        default_factory=list,
        sa_column=sa.Column(ARRAY(MutableDict.as_mutable(JSONB))),
        min_items=1,
    )
    date: datetime = Field(default=datetime.now(), include=False)
    history: int = Field(default=None, foreign_key="orderhistory.id")

    @property
    def price(self):
        return sum(pizza.price for pizza in self.pizzas)


class OrderHistoryBase(SQLModel):
    order: int = Field(default=None, foreign_key="order.id")
    date: datetime = Field(default=datetime.now(), include=False)
    status: Status = Status.VERIFICATION
