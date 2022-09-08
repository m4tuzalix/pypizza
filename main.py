from fastapi import FastAPI
from endpoints import pizza_endpoints, order_endpoints
from dependency import database
from SQL import models

models.Base.metadata.create_all(database.engine)

app = FastAPI()
app.include_router(pizza_endpoints.router, prefix="/pizza")
app.include_router(order_endpoints.router, prefix="/order")


@app.get("/")
async def welcome_page():
    return {"message": "hello"}
