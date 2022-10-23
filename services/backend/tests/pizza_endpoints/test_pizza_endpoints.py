from tests.settings import pytest, client, test_db


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", 50.0, ["cheese", "salami"]),
        ("ananas", 60.0, ["cheese", "ananas"]),
    ],
)
def test_create_pizza(test_db, name, price, ingredients):
    response = client.post(
        "/pizza/create_pizza/",
        json={"name": name, "price": price, "ingredients": ingredients},
    )
    assert response.json() == {"name": name, "price": price, "ingredients": ingredients}
    assert response.status_code == 200


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", 50.0, ["cheese"]),
        ("salama", 50.0, ["x" for x in range(10)]),
    ],
)
def test_create_pizza_with_insufficient_ingredients(test_db, name, price, ingredients):
    response = client.post(
        "/pizza/create_pizza/",
        json={"name": name, "price": price, "ingredients": ingredients},
    )
    assert response.json() != {"name": name, "price": price, "ingredients": ingredients}
    assert response.status_code != 200


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", 50.0, ["cheese", "salami"]),
    ],
)
def test_delete_exists_pizza(test_db, name, price, ingredients):
    pizza = client.post(
        "/pizza/create_pizza/",
        json={"name": name, "price": price, "ingredients": ingredients},
    )
    response = client.delete(f"/pizza/delete_pizza/{name}")
    assert response.json()["detail"] == f"{name} removed"


@pytest.mark.parametrize(
    "name",
    [
        ("salama"),
    ],
)
def test_delete_not_existing_pizza(test_db, name):
    response = client.delete(f"/pizza/delete_pizza/{name}")
    assert response.json()["detail"] == "Pizza does not exist"


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", 50.0, ["cheese", "salami"]),
    ],
)
def test_find_existing_pizza(test_db, name, price, ingredients):
    pizza = client.post(
        "/pizza/create_pizza/",
        json={"name": name, "price": price, "ingredients": ingredients},
    )
    response = client.get(f"/pizza/find_pizza/{name}")
    assert response.json()["name"] == pizza.json()["name"]


@pytest.mark.parametrize(
    "name",
    [
        ("salama"),
    ],
)
def test_find_not_existing_pizza(test_db, name):
    response = client.get(f"/pizza/find_pizza/{name}")
    assert response.json()["detail"] == f"{name} does not exist"
