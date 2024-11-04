# Exercise: Simplified Insurance Premium Calculator

## Objective
Create an `InsurancePolicy` class in Python that calculates insurance premiums based on age and smoking status, using TDD with `pytest`.

## Requirements

### Class: `InsurancePolicy`

#### Attributes
- `base_premium`: Base annual premium in USD (defaults to 500)
- `age`: Age of the insured person (in years)
- `is_smoker`: Boolean indicating if the person is a smoker

#### Methods
- `get_age_adjustment()`: Returns an additional cost based on age.
  - If `age` is over 50, returns 20% of the `base_premium`; otherwise, returns 0.
  
- `get_smoker_adjustment()`: Returns an additional cost based on smoking status.
  - If `is_smoker` is `True`, returns 30% of the `base_premium`; otherwise, returns 0.

- `calculate_premium()`: Calculates the final premium by adding the `base_premium` to the adjustments from `get_age_adjustment` and `get_smoker_adjustment`.

#### Exceptions
- Raises a `ValueError` if `age` is below 0 or above 120.

## Instructions

1. **Write Tests First**  
   Using `pytest`, create tests for each method individually. Test the final premium calculation to confirm all adjustments apply correctly.

2. **Implement the Code**  
   Implement each method in the `InsurancePolicy` class to pass the tests.


## Tests to Create

1. `test_initial_premium()`
   - Verify that `calculate_premium()` returns the `base_premium` if no adjustments apply (e.g., age is below 50 and `is_smoker` is `False`).

2. `test_age_adjustment_above_50()`
   - Verify that `get_age_adjustment()` returns 20% of the `base_premium` when `age` is over 50.

3. `test_age_adjustment_below_50()`
   - Verify that `get_age_adjustment()` returns 0 when `age` is 50 or below.

4. `test_smoker_adjustment_true()`
   - Verify that `get_smoker_adjustment()` returns 30% of the `base_premium` when `is_smoker` is `True`.

5. `test_smoker_adjustment_false()`
   - Verify that `get_smoker_adjustment()` returns 0 when `is_smoker` is `False`.

6. `test_combined_adjustments()`
   - Verify that `calculate_premium()` correctly combines adjustments when `age` is over 50 and `is_smoker` is `True`.

7. `test_invalid_age_below_zero()`
   - Verify that creating an `InsurancePolicy` instance with `age` below 0 raises a `ValueError`.

8. `test_invalid_age_above_maximum()`
   - Verify that creating an `InsurancePolicy` instance with `age` above 120 raises a `ValueError`.