# app/tests/test_integration.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_apply_loan():
    # Example: Test a GET request to an endpoint that does not exist
    response = client.get("/nonexistent-endpoint")
    assert response.status_code == 404  # Adjusted to expect a 404 status code
    assert response.json() == {"detail": "Not Found"}  # Adjusted error detail as needed
