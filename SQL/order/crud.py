from . import schemas
from dependency import Session
from .. import models
from fastapi.encoders import jsonable_encoder
from SQL.order.validations import StatusValidator, PizzaExistsValidator
from SQL.validator import validator
from SQL.pizza.crud import get_pizza

@validator(PizzaExistsValidator)
def create_order(db: Session, order: schemas.Order):
    total_price = order.price
    order.pizzas = jsonable_encoder(order.pizzas)
    db_order = models.Order(**dict(order), price=total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@validator(StatusValidator)
def update_status(db: Session, orderStatus: schemas.OrderStatus):
    db_orderStatus = models.OrderHistory(
        order = orderStatus.order_id,
        date = orderStatus.date,
        status = orderStatus.status.value
    )
    db.add(db_orderStatus)
    db.commit()
    db.refresh(db_orderStatus)
    _status_name = schemas.Status(db_orderStatus.status).name
    return {
        "order_id": db_orderStatus.order,
        "status": _status_name,
        "date": db_orderStatus.date
    }

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()