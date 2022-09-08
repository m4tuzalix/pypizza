from . import schemas
from dependency import Session
from .. import models


# Pizza
def create_pizza(db: Session, pizza: schemas.Pizza):
    db_pizza = models.Pizza(**dict(pizza))
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def get_pizza(db: Session, pizza_name: str):
    return db.query(models.Pizza).filter(models.Pizza.name == pizza_name).first()

def delete_pizza(db: Session, pizza_name: str):
    pizza = get_pizza(db, pizza_name)
    db.delete(pizza)
    db.commit()
