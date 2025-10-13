# tests/test_my_module.py
from unipackage.adder import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(10, 10) == 0