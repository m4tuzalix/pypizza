from tests import database
from dependency import get_db
from main import app
from SQL import models
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest


@pytest.fixture()
def test_db():
    models.Base.metadata.create_all(bind=database.test_engine)
    db = database.TestSessionLocal()
    yield db
    models.Base.metadata.drop_all(bind=database.test_engine)


@pytest.fixture()
def test_db_constant():
    models.Base.metadata.create_all(bind=database.test_engine)
    db = database.TestSessionLocal()
    yield db


def test_get_db():
    db = database.TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = test_get_db

client = TestClient(app)
