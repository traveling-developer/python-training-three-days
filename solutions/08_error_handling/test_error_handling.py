# test_divide_numbers.py

import pytest
from your_module import divide_numbers, InvalidInputError  # Replace `your_module` with the actual module name

# 1. Test Case: Valid division
def test_valid_division():
    result = divide_numbers(10, 2)
    assert result == 5
    assert result is not None

# 2. Test Case: Division by zero, which should return None and handle ZeroDivisionError
def test_division_by_zero():
    result = divide_numbers(10, 0)
    assert result is None

# 3. Test Case: Non-numeric numerator, which should raise InvalidInputError
def test_non_numeric_numerator():
    with pytest.raises(InvalidInputError) as exc_info:
        divide_numbers("a", 2)
    assert "Numerator and denominator must be numbers." in str(exc_info.value)

# 4. Test Case: Non-numeric denominator, which should raise InvalidInputError
def test_non_numeric_denominator():
    with pytest.raises(InvalidInputError) as exc_info:
        divide_numbers(10, "b")
    assert "Numerator and denominator must be numbers." in str(exc_info.value)

# 5. Test Case: Both numerator and denominator are non-numeric, should raise InvalidInputError
def test_both_non_numeric():
    with pytest.raises(InvalidInputError) as exc_info:
        divide_numbers("a", "b")
    assert "Numerator and denominator must be numbers." in str(exc_info.value)
