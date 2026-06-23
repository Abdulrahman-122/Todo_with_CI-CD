from fastapi.testclient import TestClient
from main.app import app

client = TestClient(app)


def get_token():
    client.post(
        "/auth/register",
        json={"username": "todo_user", "email": "todo@test.com", "password": "123456"},
    )

    response = client.post(
        "/auth/login", json={"email": "todo@test.com", "password": "123456"}
    )

    return response.json()["access_token"]


# create todo
def test_create_todo():
    token = get_token()
    res1 = client.post(
        "/todos/",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Learn FastApi", "completed": False},
    )
    assert res1.status_code == 201
    data = res1.json()
    assert data["title"] == "Learn FastApi"
    # get todo
    todo_id = res1.json()["id"]

    res2 = client.get(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {token}"})

    assert res2.status_code == 200
    assert res2.json()["id"] == todo_id


# update Todo


# Delete Todo
