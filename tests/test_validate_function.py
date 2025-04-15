import pytest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from validate_function import validate_function

def test_valid_simple_expression():
    f = validate_function("x + 2")
    assert f(3) == 5

def test_valid_math_log():
    f = validate_function("math.log(x + 1)")
    assert round(f(1), 5) == round(math.log(2), 5)

def test_valid_math_sin():
    f = validate_function("10 * math.sin(x / 5) + 50")
    assert round(f(5), 5) == round(10 * math.sin(1) + 50, 5)

def test_invalid_use_of_os():
    f = validate_function("__import__('os').system('ls')")
    assert f(5) == 5  # fallback a y=x

def test_invalid_undefined_var():
    f = validate_function("y + 2")
    assert f(5) == 5  # fallback a y=x

def test_power_function():
    f = validate_function("x**2")
    assert f(4) == 16

