from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_existing_customer():
    response = client.get("/customers/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Hassan"


def test_get_missing_customer_returns_404():
    response = client.get("/customers/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Customer not found"}
