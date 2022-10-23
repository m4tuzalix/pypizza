from sqlmodel import SQLModel, Field
from typing import List
from datetime import datetime
from SQL.pizza.schemas import PizzaBase
from SQL.order.schemas import OrderBase, OrderHistoryBase


class Pizza(PizzaBase, table=True):
    id: int = Field(default=None, primary_key=True)


class Order(OrderBase, table=True):
    id: int = Field(default=None, primary_key=True)


class OrderHistory(OrderHistoryBase, table=True):
    id: int = Field(default=None, primary_key=True)
