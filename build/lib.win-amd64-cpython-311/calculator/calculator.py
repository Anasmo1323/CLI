# src/python/calculator/calculator.py

# Import the C extension module. The leading dot makes it a relative import,
# which is crucial for it to work as part of a package.
from . import _c_calculator

class Calculator:
    """
    A class providing static methods for basic arithmetic operations.

    This class serves as a user-friendly Python wrapper around the high-performance
    C backend. It provides type hinting and Python-native error handling.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """Adds two numbers using the C backend."""
        return _c_calculator.c_add(a, b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtracts the second number from the first using the C backend."""
        return _c_calculator.c_subtract(a, b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers using the C backend."""
        return _c_calculator.c_multiply(a, b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides the first number by the second using the C backend.

        Raises:
            ZeroDivisionError: If the second number is zero. This check is
                               performed at the Python level for clarity, though
                               the C level also provides a safeguard.
        """
        if b == 0:
            raise ZeroDivisionError("Python API check: division by zero is not allowed.")
        return _c_calculator.c_divide(a, b)

    @staticmethod
    def calculate(expression: str) -> float:
        """
        Evaluates a simple string expression like 'a+b' using the C backend.

        Args:
            expression: The string expression to evaluate. Handles integers and floats.
                        Whitespace is ignored.

        Returns:
            The result of the calculation as a float.

        Raises:
            ValueError: If the expression is malformed or contains invalid numbers.
            ZeroDivisionError: If the expression involves division by zero.
        """
        return _c_calculator.c_calculate(expression)
