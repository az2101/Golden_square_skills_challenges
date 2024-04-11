
from lib.factorial import *

def test_factorial_for_5():
    criteria = 120
    result = factorial(5)
    assert criteria == result

def test_factorial_for_6():
    criteria = 720
    result = factorial(6)
    assert criteria == result

