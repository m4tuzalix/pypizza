from sqlalchemy import Column, Integer, String, Float, ARRAY, BOOLEAN, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from SQL.database import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

# Pizza
class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    ingredients = Column(ARRAY(String))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone = Column(String)
    postal_code = Column(String)
    address = Column(String)
    pizzas = Column(ARRAY(MutableDict.as_mutable(JSONB)))
    active = Column(BOOLEAN)
    date = Column(DateTime)
    price = Column(DECIMAL(10,2))
    history = relationship("OrderHistory")


class OrderHistory(Base):
    __tablename__ = "orders_history"

    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer, ForeignKey("orders.id"))
    date = Column(DateTime)
    status = Column(Integer)