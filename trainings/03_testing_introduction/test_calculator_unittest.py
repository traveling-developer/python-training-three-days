import unittest
from codes.calculator import Calculator

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup TestCalculator class resources")

    def setUp(self):
        print("Setting up a fresh Calculator instance for a test")
        pass

    def test_calculator_name(self):
        """Test that the Calculator name is set correctly."""
        pass

    def test_add(self):
        """Test addition functionality."""
        pass

    def test_subtract(self):
        """Test subtraction functionality."""
        pass

    def test_multiply(self):
        """Test multiplication functionality."""
        pass

    def test_divide(self):
        """Test division functionality."""
        pass

    def test_divide_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            pass

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestCalculator class resources")
