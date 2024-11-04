# codes/calculator.py

class Calculator:
    def __init__(self, name):
        """
        Initialize the calculator with a given name.
        """
        self.name = name

    def add(self, x, y):
        """Return the sum of x and y."""
        return x + y

    def subtract(self, x, y):
        """Return the difference of x and y."""
        return x - y

    def multiply(self, x, y):
        """Return the product of x and y."""
        return x * y

    def divide(self, x, y):
        """
        Return the division of x by y.
        Raise ZeroDivisionError if y is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
