from sqlmodel import SQLModel, Field
from typing import List, Optional
from enum import Enum

# Pizza
class PizzaSize(Enum):
    BIG = "big"
    MEDIUM = "medium"
    SMALL = "small"


class PizzaBase(SQLModel):
    name: str = Field(default=None, unique=True)
    price: float
    ingredients: List[str]


class OrderedPizza(SQLModel):
    pizza: PizzaBase
    size: Optional[PizzaSize] = PizzaSize.MEDIUM
    amount: int = 1

    @property
    def price(self):
        return self.amount * self.pizza.price
