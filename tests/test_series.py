from math_series.series import fibonacci, lucas, sum_series

# Fib tests [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibnonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_nine():
    acutal = fibonacci(9)
    expected = 34
    assert acutal == expected

# Lucas test [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]

def test_lucas_zero():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_one():
    acutal = lucas(1)
    expected = 1
    assert acutal == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_nine():
    actual = lucas(9)
    expected = 76
    assert actual ==expected

# sum series test 

def test_sum_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_two():
    acutal = sum_series(2)
    expected = 1
    assert acutal == expected

def test_sum_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_nine():
    actual = sum_series(9)
    expected =34
    assert actual == expected
