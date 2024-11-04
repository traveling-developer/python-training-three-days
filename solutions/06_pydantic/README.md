# Exercise: Validating Insurance Policy Data with Pydantic

## Background

In this exercise, you will practice using Pydantic to validate data in an insurance context. The goal is to ensure that incoming data for an insurance policy adheres to specific rules, making the application more robust and reducing the risk of errors.

Insurance policies often contain critical fields such as policy IDs, premium amounts, and the age of the insured. These fields must meet certain criteria for the policy to be valid. For example, a policy ID should be positive, a premium amount should be a positive float, and the insured person's age should fall within a reasonable range.

## Instructions

### 1. Start with the Basic Model
Define a class `InsurancePolicy` that inherits from `Pydantic.BaseModel` and includes fields for:
- `policy_id`: A positive integer representing the unique identifier for each policy.
- `premium`: A float representing the policy's monthly premium.
- `insured_age`: An integer representing the age of the insured person.

### 2. Add Custom Validators
For fields where direct constraints aren’t sufficient, add custom validation logic:
- Ensure `premium` is a positive value.
- Ensure `insured_age` is a reasonable age (for this exercise, assume ages between 18 and 100).

### 3. Test Cases

Write a few example test cases to validate the functionality:

- **Case 1**: A valid `InsurancePolicy` instance with all fields correctly filled.
- **Case 2**: An invalid policy where `policy_id` is zero, which should raise a `ValidationError` because it must be positive.
- **Case 3**: An invalid policy where `policy_id` is negative, which should raise a `ValidationError` due to the positive integer constraint.
- **Case 4**: An invalid policy where `premium` is zero, which should raise a `ValidationError` because `premium` must be a positive float.
- **Case 5**: An invalid policy where `premium` is negative, which should raise a `ValidationError` because `premium` must be positive.
- **Case 6**: An invalid policy where `insured_age` is below the allowed minimum (e.g., 17), which should raise a `ValidationError` because `insured_age` must be between 18 and 100.
- **Case 7**: A boundary test for `insured_age` set to the minimum valid age (18), which should pass as it is within the allowed range.
