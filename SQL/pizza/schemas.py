from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

# Pizza
class PizzaSize(Enum):
    BIG = "big"
    MEDIUM = "medium"
    SMALL = "small"


class Pizza(BaseModel):
    name: str
    price: float
    ingredients: List[str] = Field(default_factory=list[str], min_items=2, max_items=6)

    class Config:
        orm_mode = True

class OrderedPizza(BaseModel):
    pizza: Pizza
    size: Optional[PizzaSize] = PizzaSize.MEDIUM
    amount: int = 1

    @property
    def price(self):
        return self.amount * self.pizza.price