from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_echo():
    response = client.post("/mcp", json={"task": "echo", "payload": {"msg": "hello"}})
    assert response.status_code == 200
    assert response.json() == {"response": {"msg": "hello"}}

def test_get_time():
    response = client.post("/mcp", json={"task": "get_time", "payload": {}})
    assert response.status_code == 200
    assert "response" in response.json()
