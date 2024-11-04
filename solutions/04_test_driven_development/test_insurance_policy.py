import pytest
from insurance_policy import InsurancePolicy

def test_initial_premium():
    policy = InsurancePolicy(age=30, is_smoker=False)
    assert policy.calculate_premium() == 500

def test_age_adjustment_above_50():
    policy = InsurancePolicy(age=55, is_smoker=False)
    assert policy.get_age_adjustment() == 100  # 20% of 500

def test_age_adjustment_below_50():
    policy = InsurancePolicy(age=30, is_smoker=False)
    assert policy.get_age_adjustment() == 0

def test_smoker_adjustment():
    policy = InsurancePolicy(age=30, is_smoker=True)
    assert policy.get_smoker_adjustment() == 150  # 30% of 500

def test_non_smoker_adjustment():
    policy = InsurancePolicy(age=30, is_smoker=False)
    assert policy.get_smoker_adjustment() == 0

def test_combined_adjustments():
    policy = InsurancePolicy(age=55, is_smoker=True)
    assert policy.calculate_premium() == 750  # 500 + 100 + 150

def test_invalid_age_below_zero():
    with pytest.raises(ValueError):
        InsurancePolicy(age=-5, is_smoker=False)

def test_invalid_age_above_maximum():
    with pytest.raises(ValueError):
        InsurancePolicy(age=130, is_smoker=False)
