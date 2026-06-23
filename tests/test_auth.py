from fastapi.testclient import TestClient
from main.app import app

client = TestClient(app)


def test_register():
    res = client.post(
        "/auth/register",
        json={
            "username": "John6",
            "email": "john6@demo.com",
            "password": "TTYSrecrets",
        },
    )
    assert res.status_code == 201


def test_login():
    res = client.post(
        "/auth/login", json={"email": "john6@demo.com", "password": "TTYSrecrets"}
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
