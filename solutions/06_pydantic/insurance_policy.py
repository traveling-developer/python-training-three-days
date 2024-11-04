from pydantic import BaseModel, PositiveInt, field_validator

class InsurancePolicy(BaseModel):
    policy_id: PositiveInt
    premium: float
    insured_age: int

    @field_validator('premium')
    def check_premium(cls, value):
        if value <= 0:
            raise ValueError('Premium must be a positive number')
        return value

    @field_validator('insured_age')
    def check_age(cls, value):
        if not 18 <= value <= 100:
            raise ValueError('Insured age must be between 18 and 100')
        return value
