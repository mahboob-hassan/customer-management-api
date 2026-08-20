from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

<<<<<<< Updated upstream
=======
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

>>>>>>> Stashed changes
def test_get_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_customer_found():
    response = client.get("/customers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Hassan"

def test_create_customer():
    payload = {
        "name" : "Mike",
        "email" : "mike@example.com",
        "city" : "Boston"
    }

    response = client.post("/customers/", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Mike"
    assert data["email"] == "mike@example.com"
    assert data["city"] == "Boston"
