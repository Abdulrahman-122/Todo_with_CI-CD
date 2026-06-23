from fastapi.testclient import TestClient
from main.app import app
import uuid
import pytest

client = TestClient(app)


@pytest.fixture
def test_user():
    email = f"john{uuid.uuid4()}@demo.com"
    password = "TTYSrecrets"
    username = "John"

    # register user
    res = client.post(
        "/auth/register",
        json={
            "username": username,
            "email": email,
            "password": password,
        },
    )
    assert res.status_code == 201

    return {
        "email": email,
        "password": password
    }


def test_register():
    email = f"john{uuid.uuid4()}@demo.com"

    res = client.post(
        "/auth/register",
        json={
            "username": "John",
            "email": email,
            "password": "TTYSrecrets",
        },
    )

    assert res.status_code == 201


def test_login(test_user):
    res = client.post(
        "/auth/login",
        json={
            "email": test_user["email"],
            "password": test_user["password"],
        },
    )

    assert res.status_code == 200
    data = res.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"