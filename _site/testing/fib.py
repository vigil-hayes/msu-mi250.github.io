import pytest
import datetime


def fib(n):
    if n <= 2:
        return 1
    return (fib(n-1) + fib(n-2))


# Level 0 tests
def test_fib_3():
    assert fib(4) == 3


# Level 1 tests
def test_fib_1():
    assert fib(1) == 1

def test_fib_2():
    assert fib(2) == 1

def test_fib_10():
    assert fib(10) == 55


# Level 2 tests
def test_fib_negative():
    with pytest.raises(IndexError):
        fib(-1)

def test_fib_fraction():
    with pytest.raises(IndexError):
        fib(2.5)

def test_fib_string():
    with pytest.raises(IndexError):
        fib("hi")

# Level 3 tests
def test_fib_speed():
    start = datetime.datetime.now()
    out = fib(40)
    end = datetime.datetime.now()
    assert (end-start).total_seconds() < 10  # It should take less than 10 seconds to compute


