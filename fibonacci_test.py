def test_generate_fibonacci_series():
    assert generate_fibonacci_series(0) == [], "Test case for n=0 failed"
    assert generate_fibonacci_series(1) == [0], "Test case for n=1 failed"
    assert generate_fibonacci_series(2) == [0, 1], "Test case for n=2 failed"
    assert generate_fibonacci_series(5) == [0, 1, 1, 2, 3], "Test case for n=5 failed"
    assert generate_fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Test case for n=10 failed"

# Call the test function
test_generate_fibonacci_series()