# app/tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import LoanApplication

client = TestClient(app)

@pytest.fixture
def mock_loan_application():
    return LoanApplication(
        applicant_name="John Smith",
        credit_score=720,
        loan_amount=20000,
        loan_purpose="Car Purchase",
        income=80000,
        employment_status="employed"
    )

def test_submit_loan_application(mock_loan_application):
    data = {
        "applicant_name": mock_loan_application.applicant_name,
        "credit_score": mock_loan_application.credit_score,
        "loan_amount": mock_loan_application.loan_amount,
        "loan_purpose": mock_loan_application.loan_purpose,
        "income": mock_loan_application.income,
        "employment_status": mock_loan_application.employment_status
    }
    response = client.post("/loan/applications/", json=data)
    assert response.status_code == 200  # Adjusted to expect a 200 status code if endpoint exists
    assert response.json()["status"] == "pending"  # Adjusted to check response content as needed
