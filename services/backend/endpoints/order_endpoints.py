from fastapi import APIRouter, Depends, HTTPException
from dependency import Session, get_db
from SQL.order import crud
from SQL import models
from SQL.database import get_session, AsyncSession
from SQL.order.exceptions import WrongStatusException, PizzaExistenceException

router = APIRouter()


@router.post("/create_order/", status_code=201)
async def create_order(
    order: models.OrderBase, db: AsyncSession = Depends(get_session)
):
    try:
        return crud.create_order(db, order)
    except PizzaExistenceException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/get_order/{order_id}", status_code=200)
async def get_order(order_id: int, db: AsyncSession = Depends(get_session)):
    order = crud.get_order(db, order_id)
    if order:
        return {"order_id": order_id, "details": order}
    raise HTTPException(status_code=404, detail="Order not found")


@router.post("/update_status/", status_code=201)
async def update_status(
    orderStatus: models.OrderBase, db: AsyncSession = Depends(get_session)
):
    message_error = "Order not found"
    if order := crud.get_order(db, orderStatus.order_id):
        try:
            return crud.update_status(db, orderStatus)
        except WrongStatusException as e:
            message_error = e.message
    raise HTTPException(status_code=404, detail=message_error)
