# Test cases for generate_fibonacci_series

def test_generate_fibonacci_series():
    # Test case 1: n = 0
    assert generate_fibonacci_series(0) == []
    
    # Test case 2: n = 1
    assert generate_fibonacci_series(1) == [0]
    
    # Test case 3: n = 2
    assert generate_fibonacci_series(2) == [0, 1]
    
    # Test case 4: n = 5
    assert generate_fibonacci_series(5) == [0, 1, 1, 2, 3]
    
    print('All test cases pass successfully!')