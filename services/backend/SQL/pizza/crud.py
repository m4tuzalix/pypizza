from dependency import Session
from SQL.database import AsyncSession
from SQL import models


# Pizza
def create_pizza(db: AsyncSession, pizza: models.PizzaBase):
    db_pizza = models.Pizza(**dict(pizza))
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza


def get_pizza(db: AsyncSession, pizza_name: str):
    return db.query(models.Pizza).filter(models.Pizza.name == pizza_name).first()


def get_all_pizzas(db: AsyncSession):
    return db.query(models.Pizza).all()


def delete_pizza(db: AsyncSession, pizza_name: str):
    pizza = get_pizza(db, pizza_name)
    db.delete(pizza)
    db.commit()
