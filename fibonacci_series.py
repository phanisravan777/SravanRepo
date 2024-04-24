def generate_fibonacci_series(n):
    """
    Generate the Fibonacci series up to the n-th term.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    list: A list containing the Fibonacci series up to the n-th term.
    """
    # Base cases: if n is 0 or 1, return the corresponding Fibonacci series
    if n == 0:
        return []
    elif n == 1:
        return [0]

    # Initialize the first two terms of the Fibonacci series
    fib_series = [0, 1]

    # Generate the Fibonacci series up to the n-th term
    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)

    return fib_series

# Testing the function with provided input and validating the expected output
input_data = [[0], [1], [2], [5]]
expected_output = [[], [0], [0, 1], [0, 1, 1, 2, 3]]

for i in range(len(input_data)):
    assert generate_fibonacci_series(*input_data[i]) == expected_output[i], f'Test case {i+1} failed'

print('All test cases passed successfully.')