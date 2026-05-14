from fastapi.testclient import TestClient
from app import app
import pytest

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Empathy Chatbot API is running!"}

def test_chat_endpoint_structure():
    # We send a tiny request just to verify the endpoint accepts it and returns the correct schema
    # We won't test the actual AI response generation here because it takes too long for a quick CI/CD test
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    assert "response" in response.json()
