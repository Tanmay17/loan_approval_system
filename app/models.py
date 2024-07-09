from pydantic import BaseModel, Field
from enum import Enum

class EmploymentStatus(str, Enum):
    employed = "employed"
    unemployed = "unemployed"
    self_employed = "self_employed"

class LoanApplication(BaseModel):
    applicant_name: str = Field(..., example="John Doe")
    credit_score: int = Field(..., example=700, ge=300, le=850)
    loan_amount: float = Field(..., example=10000, gt=0)
    loan_purpose: str = Field(..., example="Home Improvement")
    income: float = Field(..., example=50000, gt=0)
    employment_status: EmploymentStatus
    other_info: str = Field(None, example="Additional relevant information")
