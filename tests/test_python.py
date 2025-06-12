import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0

def test_subtract():
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(5, 10) == -5

def test_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-3, 4) == -12

def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

def test_calculate_simple():
    assert Calculator.calculate("5+3") == 8.0
    assert Calculator.calculate("10-2") == 8.0
    assert Calculator.calculate("4*5") == 20.0
    assert Calculator.calculate("20/4") == 5.0

def test_calculate_with_floats_and_spaces():
    assert Calculator.calculate(" 2.5 + 2.5 ") == 5.0
    assert Calculator.calculate(" 1.2 * 10 ") == 12.0

def test_calculate_with_negative_numbers():
    assert Calculator.calculate("-5+10") == 5.0
    assert Calculator.calculate("5+-2") == 3.0
    assert Calculator.calculate("-5*-5") == 25.0

def test_calculate_invalid_expression():
    with pytest.raises(ValueError):
        Calculator.calculate("5+