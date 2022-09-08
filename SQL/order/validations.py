from SQL.order import schemas
from dependency import Session
from SQL import models
from SQL.order.exceptions import WrongStatusException, PizzaExistenceException
from SQL.pizza.crud import get_pizza

class PizzaExistsValidator:
    def __init__(self, order: schemas.Order):
        self.order = order
    def validation(self, db: Session):
        if not all(get_pizza(db, ordered_pizza.pizza.name) != None
                   for ordered_pizza in self.order.pizzas):
            return PizzaExistenceException("Pizza does not exist")

class StatusValidator:
    def __init__(self, orderStatus: schemas.OrderStatus):
        self.orderStatus = orderStatus
    def validation(self, db: Session):
        """status must be unique and put in order: 1,2,3,4 etc not 1,3,4"""
        _status = self.orderStatus.status.value

        history = (db
        .query(models.OrderHistory)
        .filter(
            models.OrderHistory.order == self.orderStatus.order_id,
        )
        ).all()

        if not history:
            if _status > 1: return WrongStatusException("First status must be VERIFICATION")
        else:
            statuses = [obj.status for obj in history]
            if _status in statuses: return WrongStatusException("This status is already implemented")
            if (_status - max(statuses)) > 1: return WrongStatusException("Wrong status order")
