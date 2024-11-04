import pytest
from codes.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to initialize Calculator instance with a name."""
    return Calculator(name="TestCalculator")

def test_calculator_name(calculator):
    """Test that the Calculator name is set correctly."""
    assert calculator.name == "TestCalculator"

def test_add(calculator):
    """Test addition functionality."""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract(calculator):
    """Test subtraction functionality."""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 3) == -3

def test_multiply(calculator):
    """Test multiplication functionality."""
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-1, -1) == 1

def test_divide(calculator):
    """Test division functionality."""
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(-6, -2) == 3

def test_divide_by_zero(calculator):
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
