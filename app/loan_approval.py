def approve_loan(risk_score: float, minimum_risk_score: float = 50) -> bool:
    return risk_score >= minimum_risk_score
