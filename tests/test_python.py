import pytest
from calculator import Calculator
# A tolerance for float comparisons
TOLERANCE = 1e-9

# --- Test direct API calls ---

def test_add():
    assert abs(Calculator.add(2, 3) - 5.0) < TOLERANCE
    assert abs(Calculator.add(-1, 1) - 0.0) < TOLERANCE
    assert abs(Calculator.add(1.2, 3.4) - 4.6) < TOLERANCE

def test_subtract():
    assert abs(Calculator.subtract(10, 5) - 5.0) < TOLERANCE
    assert abs(Calculator.subtract(5, 10) - -5.0) < TOLERANCE

def test_multiply():
    assert abs(Calculator.multiply(3, 4) - 12.0) < TOLERANCE
    assert abs(Calculator.multiply(-3, 4) - -12.0) < TOLERANCE

def test_divide():
    assert abs(Calculator.divide(10, 2) - 5.0) < TOLERANCE
    assert abs(Calculator.divide(5, 2) - 2.5) < TOLERANCE

def test_divide_by_zero_api():
    """Test that the Python API wrapper raises the correct exception."""
    with pytest.raises(ZeroDivisionError, match="Python API check"):
        Calculator.divide(10, 0)

# --- Test string expression evaluation ---

def test_calculate_simple_expressions():
    assert abs(Calculator.calculate("5+3") - 8.0) < TOLERANCE
    assert abs(Calculator.calculate("10-2") - 8.0) < TOLERANCE
    assert abs(Calculator.calculate("4*5") - 20.0) < TOLERANCE
    assert abs(Calculator.calculate("20/4") - 5.0) < TOLERANCE

def test_calculate_with_floats_and_spaces():
    assert abs(Calculator.calculate(" 2.5 + 2.5 ") - 5.0) < TOLERANCE
    assert abs(Calculator.calculate(" 1.2 * 10 ") - 12.0) < TOLERANCE

def test_calculate_with_negative_numbers():
    assert abs(Calculator.calculate("-5+10") - 5.0) < TOLERANCE
    assert abs(Calculator.calculate("5+-2") - 3.0) < TOLERANCE
    assert abs(Calculator.calculate("-5*-5") - 25.0) < TOLERANCE

def test_calculate_divide_by_zero_expression():
    """Test that the C backend correctly raises an exception for /0 in an expression."""
    with pytest.raises(ZeroDivisionError, match="C-level check"):
        Calculator.calculate("1/0")

def test_calculate_invalid_expressions():
    """Test malformed expressions that should raise ValueErrors."""
    with pytest.raises(ValueError, match="Invalid expression: operator not found"):
        Calculator.calculate("5 5")

    with pytest.raises(ValueError, match="Invalid number format"):
        Calculator.calculate("5++5")

    with pytest.raises(ValueError, match="Invalid number format"):
        Calculator.calculate("a+5")

    with pytest.raises(ValueError, match="Invalid expression: operator not found"):
        Calculator.calculate("10")
