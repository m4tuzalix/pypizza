from tests.settings import pytest, client

@pytest.fixture()
def pizza():
    return {
        "name": "salama",
        "price": 23.50,
        "ingredients": ["salami", "cheese"]
    }

@pytest.fixture()
def correct_order(pizza):
    return {
        "name": "some_name",
        "surname": "some_surname",
        "email": "test@gmail.com",
        "phone": "111111111",
        "postal_code": "11-111",
        "address": "some address",
        "pizzas": [{"pizza": pizza, "size": "big", "amount": 1}]
    }

@pytest.fixture()
def db_pizza(pizza):
    client.post("/pizza/create_pizza/", json=pizza)

@pytest.fixture()
def db_order(db_pizza, correct_order):
    return client.post("/order/create_order/", json=correct_order).json()["id"]