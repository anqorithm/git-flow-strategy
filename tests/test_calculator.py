from src.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(2, 5) == -3
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-1, 3) == -3
    assert calculator.multiply(0, 100) == 0