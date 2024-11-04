import pytest
from codes.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to initialize Calculator instance with a name."""
    pass

def test_calculator_name(calculator):
    """Test that the Calculator name is set correctly."""
    pass

def test_add(calculator):
    """Test addition functionality."""
    pass

def test_subtract(calculator):
    """Test subtraction functionality."""
    pass

def test_multiply(calculator):
    """Test multiplication functionality."""
    pass

def test_divide(calculator):
    """Test division functionality."""
    pass

def test_divide_by_zero(calculator):
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        pass
