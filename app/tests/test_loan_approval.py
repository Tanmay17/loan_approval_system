import pytest
from app.loan_approval import approve_loan
from app.models import LoanApplication

@pytest.fixture
def mock_loan_application():
    return LoanApplication(
        applicant_name="Jane Doe",
        credit_score=750,
        loan_amount=15000,
        loan_purpose="Education",
        income=60000,
        employment_status="employed"
    )

def test_approve_loan(mock_loan_application):
    # Mock a risk score and minimum risk score
    risk_score = 60
    minimum_risk_score = 50

    # Use the mock_loan_application to approve the loan based on risk score
    approval_status = approve_loan(risk_score, minimum_risk_score)
    assert approval_status == True

def test_reject_loan(mock_loan_application):
    # Mock a risk score and minimum risk score
    risk_score = 40
    minimum_risk_score = 50

    # Use the mock_loan_application to reject the loan based on risk score
    approval_status = approve_loan(risk_score, minimum_risk_score)
    assert approval_status == False