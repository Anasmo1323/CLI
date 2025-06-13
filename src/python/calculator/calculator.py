# src/python/calculator/calculator.py
# Import the C extension module. The leading dot makes it a relative import.
from . import _c_calculator

class Calculator:
    """
    A class providing static methods for basic arithmetic operations, serving as a
    Python interface to a high-performance C backend. This class wraps C functions
    using the C-Python API, offering type hinting and Python-native error handling
    for ease of use in both API and command-line contexts.

    Note:
        All methods are static, so no instance of the class is required. Use them
        directly, e.g., ``Calculator.add(2.5, 3.7)``.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Adds two numbers using the C backend.

        Args:
            a (float): The first number to add.
            b (float): The second number to add.

        Returns:
            float: The sum of ``a`` and ``b``.

        Example:
            >>> Calculator.add(2.5, 3.7)
            6.2
        """
        return _c_calculator.c_add(a, b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Subtracts the second number from the first using the C backend.

        Args:
            a (float): The number to subtract from (minuend).
            b (float): The number to subtract (subtrahend).

        Returns:
            float: The result of ``a - b``.

        Example:
            >>> Calculator.subtract(5.0, 2.0)
            3.0
        """
        return _c_calculator.c_subtract(a, b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiplies two numbers using the C backend.

        Args:
            a (float): The first number (multiplicand).
            b (float): The second number (multiplier).

        Returns:
            float: The product of ``a`` and ``b``.

        Example:
            >>> Calculator.multiply(4.0, 3.0)
            12.0
        """
        return _c_calculator.c_multiply(a, b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides the first number by the second using the C backend.

        Args:
            a (float): The number to divide (dividend).
            b (float): The number to divide by (divisor). Must not be zero.

        Returns:
            float: The result of ``a / b``.

        Raises:
            ZeroDivisionError: If ``b`` is zero. This check is performed at the
                Python level for clarity, with an additional safeguard in the C backend.

        Example:
            >>> Calculator.divide(10.0, 2.0)
            5.0
            >>> Calculator.divide(5.0, 0.0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Python API check: division by zero is not allowed.
        """
        if b == 0:
            raise ZeroDivisionError("Python API check: division by zero is not allowed.")
        return _c_calculator.c_divide(a, b)

    @staticmethod
    def calculate(expression: str) -> float:
        """
        Evaluates a simple arithmetic expression provided as a string, using the C backend.

        The expression should be in the format ``number operator number``, where:
        - Numbers can be integers or floats (e.g., ``2``, ``3.14``).
        - Operators are ``+``, ``-``, ``*``, or ``/``.
        - Whitespace is ignored (e.g., ``2 + 3`` is equivalent to ``2+3``).

        Args:
            expression (str): The arithmetic expression to evaluate (e.g., ``"2 + 3"``).

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression is malformed (e.g., invalid numbers or operators).
            ZeroDivisionError: If the expression involves division by zero.

        Examples:
            >>> Calculator.calculate("2 + 3")
            5.0
            >>> Calculator.calculate("10.5 * 2")
            21.0
            >>> Calculator.calculate("5 / 0")
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Division by zero
            >>> Calculator.calculate("2 # 3")
            Traceback (most recent call last):
                ...
            ValueError: Invalid operator
        """
        return _c_calculator.c_calculate(expression)