from tests.settings import test_db_constant, test_db
from tests.order_fixtures import pytest, client, db_order, db_pizza, correct_order, pizza
from datetime import datetime
from SQL.order.exceptions import PizzaExistenceException
from fastapi import HTTPException
from SQL.order.schemas import Status

@pytest.fixture()
def incorrect_order_empty_pizzas(correct_order):
    correct_order["pizzas"] = []
    return correct_order

def test_create_correct_order(test_db, db_pizza, correct_order):
    response = client.post("/order/create_order/", json=correct_order)
    assert all(response.json()[k] == v for k,v in correct_order.items())
    assert response.json().get("date") != None
    assert response.json().get("active") == True

def test_create_incorrect_order_with_empty_pizzas(test_db, db_pizza, incorrect_order_empty_pizzas):
    response = client.post("/order/create_order/", json=incorrect_order_empty_pizzas)
    assert response.json()["detail"][0]["type"] == "value_error.list.min_items"
    assert response.status_code == 422

def test_create_incorrect_order_with_not_existing_pizza(test_db, correct_order):
    response = client.post("/order/create_order/", json=correct_order)
    assert response.json()["detail"] == "Pizza does not exist"
    assert response.status_code == 404

def test_existing_order(test_db, db_order, correct_order):
    response = client.get(f"/order/get_order/{db_order}")
    assert response.json()["order_id"] == db_order
    assert all(response.json()["details"][k] == v for k,v in correct_order.items())
    assert response.status_code == 200

def test_not_existing_order(test_db):
    response = client.get("/order/get_order/999")
    assert response.json()["detail"] == "Order not found"
    assert response.status_code == 404

@pytest.mark.parametrize("status_id", [([1,2,3,4,5])])
def test_order_updatestatus_using_correct_ordering(test_db, db_order, status_id):
    for id in status_id:
        response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": id})
        assert response.json()["order_id"] == 1
        assert response.json()["status"] == Status(id).name

def test_order_updatestatus_using_incorrect_ordering(test_db, db_order):
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 1})
    assert response.json()["order_id"] == 1
    assert response.json()["status"] == Status(1).name
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 2})
    assert response.json()["order_id"] == 1
    assert response.json()["status"] == Status(2).name
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 4})
    assert response.json()["detail"] == "Wrong status order"

def test_order_updatestatus_using_twice_the_same_status(test_db, db_order):
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 1})
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 1})
    assert response.json()["detail"] == "This status is already implemented"

def test_order_updatestatus_using_wrong_first_required_status(test_db, db_order):
    response = client.post(f"/order/update_status/", json={"order_id": db_order, "status": 2})
    assert response.json()["detail"] == "First status must be VERIFICATION"