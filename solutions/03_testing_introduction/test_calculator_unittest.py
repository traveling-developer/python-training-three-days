import unittest
from codes.calculator import Calculator

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestCalculator class resources")
        cls.calculator_name = "TestCalculator"  # Class-wide setup

    def setUp(self):
        print("Setting up a fresh Calculator instance for a test")
        self.calculator = Calculator(name=self.calculator_name)  # Create Calculator with name parameter

    def test_calculator_name(self):
        """Test that the Calculator name is set correctly."""
        self.assertEqual(self.calculator.name, self.calculator_name)

    def test_add(self):
        """Test addition functionality."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        """Test subtraction functionality."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 3), -3)

    def test_multiply(self):
        """Test multiplication functionality."""
        self.assertEqual(self.calculator.multiply(4, 3), 12)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)

    def test_divide(self):
        """Test division functionality."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-6, -2), 3)

    def test_divide_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestCalculator class resources")
