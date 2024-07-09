from fastapi import FastAPI, HTTPException
from .models import LoanApplication
from .risk_assessment import calculate_risk_score
from .loan_approval import approve_loan
from .db import save_application, get_application, update_application_status
from .queue import publish_message, consume_messages
import uuid

app = FastAPI()

@app.post("/loan/applications/")
async def submit_loan_application(application: LoanApplication):
    application_id = str(uuid.uuid4())
    debt_to_income_ratio = application.loan_amount / application.income
    risk_score = calculate_risk_score(
        application.credit_score,
        debt_to_income_ratio,
        application.employment_status,
        application.loan_amount,
        application.loan_purpose
    )
    is_approved = approve_loan(risk_score, minimum_risk_score=50)  # Example criterion
    save_application(application_id, application, risk_score, is_approved)
    publish_message(application_id)
    return {"status": "pending"}

@app.get("/status/{application_id}")
async def get_status(application_id: str):
    application = get_application(application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@app.put("/update/{application_id}")
async def update_status(application_id: str, approved: bool):
    update_application_status(application_id, approved)
    return {"application_id": application_id, "approved": approved}
