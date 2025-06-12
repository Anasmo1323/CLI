# src/python/calculator/calculator.py
from ._c_calculator import (
    c_add, c_subtract, c_multiply, c_divide, c_calculate
)

class Calculator:
    """A class providing static methods for basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Adds two numbers using the C backend."""
        return c_add(a, b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtracts two numbers using the C backend."""
        return c_subtract(a, b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers using the C backend."""
        return c_multiply(a, b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides two numbers using the C backend.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Python-level check: Cannot divide by zero")
        return c_divide(a, b)

    @staticmethod
    def calculate(expression: str) -> float:
        """
        Evaluates a simple string expression like 'a+b' using the C backend.

        Args:
            expression: The string expression to evaluate.

        Returns:
            The result of the calculation.

        Raises:
            ValueError: If the expression is malformed.
            ZeroDivisionError: If the expression involves division by zero.
        """
        return c_calculate(expression)