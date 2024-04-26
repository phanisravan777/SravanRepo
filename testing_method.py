# Test cases for generate_fibonacci_series

def test_generate_fibonacci_series_unitTest():
    assert generate_fibonacci_series(0) == []
    assert generate_fibonacci_series(1) == [0]
    assert generate_fibonacci_series(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]