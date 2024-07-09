import pytest
from app.risk_assessment import calculate_risk_score

def test_calculate_risk_score():
    # Test with standard parameters
    score = calculate_risk_score(700, 0.2, "employed", 10000, "Home Improvement")
    assert score > 0
    assert score <= 1000  # Assuming reasonable upper limit for risk score

    # Test with very high debt-to-income ratio
    score = calculate_risk_score(700, 0.8, "employed", 10000, "Home Improvement")
    assert score > 0

    # Test with very large loan amount
    score = calculate_risk_score(700, 0.2, "employed", 1000000, "Home Improvement")
    assert score > 0

    # Test with unemployed status
    score = calculate_risk_score(700, 0.2, "unemployed", 10000, "Home Improvement")
    assert score > 0

    # Test with self-employed status
    score = calculate_risk_score(700, 0.2, "self_employed", 10000, "Home Improvement")
    assert score > 0

    # Test with zero income (should not result in negative score)
    score = calculate_risk_score(700, 1.0, "unemployed", 10000, "Home Improvement")
    assert score >= 10
