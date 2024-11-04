import pytest
from pydantic import ValidationError
from insurance_policy import InsurancePolicy  # Replace with actual import path

# 1. Valid Case
def test_valid_policy():
    policy = InsurancePolicy(policy_id=1, premium=100.50, insured_age=30)
    assert policy.policy_id == 1
    assert policy.premium == 100.50
    assert policy.insured_age == 30

# 2. Invalid Policy ID - Negative and Zero
def test_invalid_policy_id_zero():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=0, premium=100.50, insured_age=30)
    assert "Policy ID must be a positive integer" in str(exc_info.value)

def test_invalid_policy_id_negative_one():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=-1, premium=100.50, insured_age=30)
    assert "Policy ID must be a positive integer" in str(exc_info.value)

def test_invalid_policy_id_negative_hundred():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=-100, premium=100.50, insured_age=30)
    assert "Policy ID must be a positive integer" in str(exc_info.value)

# 3. Invalid Premium - Negative and Zero
def test_invalid_premium_zero():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=0, insured_age=30)
    assert "Premium must be a positive number" in str(exc_info.value)

def test_invalid_premium_negative_ten():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=-10, insured_age=30)
    assert "Premium must be a positive number" in str(exc_info.value)

def test_invalid_premium_negative_fifty_point_five():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=-50.5, insured_age=30)
    assert "Premium must be a positive number" in str(exc_info.value)

# 4. Invalid Insured Age - Below 18 and Above 100
def test_invalid_insured_age_below_18():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=100.50, insured_age=17)
    assert "Insured age must be between 18 and 100" in str(exc_info.value)

def test_invalid_insured_age_above_100():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=100.50, insured_age=101)
    assert "Insured age must be between 18 and 100" in str(exc_info.value)

def test_invalid_insured_age_far_above_100():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=100.50, insured_age=150)
    assert "Insured age must be between 18 and 100" in str(exc_info.value)

# 5. Boundary Tests for Insured Age - 18 and 100 (should be valid)
def test_valid_insured_age_boundary_18():
    policy = InsurancePolicy(policy_id=1, premium=100.50, insured_age=18)
    assert policy.insured_age == 18

def test_valid_insured_age_boundary_100():
    policy = InsurancePolicy(policy_id=1, premium=100.50, insured_age=100)
    assert policy.insured_age == 100

# 6. Optional Beneficiary Name - Empty or Whitespace
def test_invalid_beneficiary_name_empty():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=100.50, insured_age=30, beneficiary_name="")
    assert "Beneficiary name must not be empty or whitespace" in str(exc_info.value)

def test_invalid_beneficiary_name_whitespace():
    with pytest.raises(ValidationError) as exc_info:
        InsurancePolicy(policy_id=1, premium=100.50, insured_age=30, beneficiary_name="   ")
    assert "Beneficiary name must not be empty or whitespace" in str(exc_info.value)

# 7. Valid Beneficiary Name
def test_valid_beneficiary_name():
    policy = InsurancePolicy(policy_id=1, premium=100.50, insured_age=30, beneficiary_name="John Doe")
    assert policy.beneficiary_name == "John Doe"
