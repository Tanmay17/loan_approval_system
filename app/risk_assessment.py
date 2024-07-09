def calculate_risk_score(credit_score: int, debt_to_income_ratio: float, employment_status: str, loan_amount: float, loan_purpose: str) -> float:
    # Start with a base score from credit score
    score = credit_score * 0.4

    # Adjust score based on debt-to-income ratio
    score += (1 - debt_to_income_ratio) * 100 * 0.3

    # Adjust score based on employment status
    if employment_status == "employed":
        score += 20
    elif employment_status == "self_employed":
        score += 10
    elif employment_status == "unemployed":
        score -= 10

    # Adjust score based on loan amount
    score -= loan_amount * 0.001

    # Ensure score does not go below a certain threshold (e.g., 10)
    score = max(score, 10)

    return score