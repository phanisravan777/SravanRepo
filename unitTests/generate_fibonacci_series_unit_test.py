def test_generate_fibonacci_series():
    assert generate_fibonacci_series(0) == []
    assert generate_fibonacci_series(1) == [0]
    assert generate_fibonacci_series(2) == [0, 1]
    assert generate_fibonacci_series(5) == [0, 1, 1, 2, 3]