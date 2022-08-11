from rest_api.app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_index():
    # Empty
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_post():
    # Add
    response = client.post("/todos", json={"content": "test", "done": False})
    assert response.status_code == 200
    assert list(response.json().values())[0] == {"content": "test", "done": False}
