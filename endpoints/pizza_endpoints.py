from fastapi import APIRouter, Depends, HTTPException
from dependency import Session, get_db
from SQL.pizza import crud, schemas
from sqlalchemy.orm.exc import UnmappedInstanceError

router = APIRouter()


@router.post("/create_pizza/", response_model=schemas.Pizza)
async def create_pizza(pizza: schemas.Pizza, db: Session = Depends(get_db)):
    if crud.get_pizza(db, pizza.name):
        raise HTTPException(status_code=400, detail="Pizza with this name has already been created")
    return crud.create_pizza(db, pizza)

@router.get("/find_pizza/{name}")
async def find_pizza(name: str, db: Session = Depends(get_db)):
    if pizza := crud.get_pizza(db, name):
        return pizza
    raise HTTPException(status_code=400, detail=f"{name} does not exist")

@router.delete("/delete_pizza/{name}")
async def delete_pizza(name: str, db: Session = Depends(get_db)):
    try:
        crud.delete_pizza(db, name)
        return {"detail": f"{name} removed"}
    except UnmappedInstanceError as e:
        return HTTPException(status_code=400, detail="Pizza does not exist")
