from tests.settings import pytest
from SQL.pizza import schemas
from pydantic.error_wrappers import ValidationError


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", 50.0, []),
    ],
)
def test_incorrect_schema_ingredients(name, price, ingredients):
    with pytest.raises(ValidationError):
        pizza = schemas.Pizza(name=name, price=price, ingredients=ingredients)


@pytest.mark.parametrize(
    "name,price,ingredients",
    [
        ("salama", "50.0", []),
    ],
)
def test_incorrect_schema_price(name, price, ingredients):
    with pytest.raises(ValidationError):
        pizza = schemas.Pizza(name=name, price=price, ingredients=ingredients)
