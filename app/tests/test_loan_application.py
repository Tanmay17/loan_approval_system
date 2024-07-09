import pytest
from app.models import LoanApplication

def test_loan_application_creation():
    application = LoanApplication(
        applicant_name="John Doe",
        credit_score=700,
        loan_amount=10000,
        loan_purpose="Home Improvement",
        income=50000,
        employment_status="employed"
    )
    assert application.applicant_name == "John Doe"
    assert application.credit_score == 700
    assert application.loan_amount == 10000
    assert application.loan_purpose == "Home Improvement"
    assert application.income == 50000
    assert application.employment_status == "employed"
