from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from SQL.pizza.schemas import OrderedPizza
from typing import List, Optional
from enum import Enum, auto


class Status(Enum):
    VERIFICATION = auto()
    ACCEPTED = auto()
    IN_PROGRESS = auto()
    IN_TRANSPORT = auto()
    DELIVERED = auto()


class Order(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: str = Field(min_length=9, max_length=9)
    postal_code: str = Field(min_length=6, max_length=6)
    address: str
    pizzas: List[OrderedPizza] = Field(min_items=1)
    active: bool = Field(default=True, include=False)
    date: datetime = Field(default=datetime.now(), include=False)

    @property
    def price(self):
        return sum(pizza.price for pizza in self.pizzas)

class OrderStatus(BaseModel):
    order_id: int
    status: Status = Status.VERIFICATION
    date: datetime = Field(default=datetime.now(), include=False)