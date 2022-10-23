from fastapi import APIRouter, Depends, HTTPException
from dependency import Session, get_db
from SQL.database import get_session, AsyncSession
from SQL.pizza import crud
from SQL import models
from sqlalchemy.orm.exc import UnmappedInstanceError

router = APIRouter()


@router.post("/create_pizza/", response_model=models.PizzaBase)
async def create_pizza(
    pizza: models.PizzaBase, db: AsyncSession = Depends(get_session)
):
    if crud.get_pizza(db, pizza.name):
        raise HTTPException(
            status_code=400, detail="Pizza with this name has already been created"
        )
    return crud.create_pizza(db, pizza)


@router.get("/find_pizza/{name}")
async def find_pizza(name: str, db: AsyncSession = Depends(get_session)):
    if pizza := crud.get_pizza(db, name):
        return pizza
    raise HTTPException(status_code=400, detail=f"{name} does not exist")


@router.get("/pizzas/")
async def get_pizzas(db: AsyncSession = Depends(get_session)):
    pizzas = crud.get_all_pizzas(db)
    if pizzas:
        print(pizzas)
        return pizzas
    raise HTTPException(status_code=400, detail="No pizzas found")


@router.delete("/delete_pizza/{name}")
async def delete_pizza(name: str, db: AsyncSession = Depends(get_session)):
    try:
        crud.delete_pizza(db, name)
        return {"detail": f"{name} removed"}
    except UnmappedInstanceError as e:
        return HTTPException(status_code=400, detail="Pizza does not exist")
