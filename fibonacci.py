# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_series = [0, 1]
    
    # Check if the user wants at least one term
    if n <= 0:
        return []
    # Return only the first term if n is 1
    elif n == 1:
        return [0]
    # Generate the Fibonacci series up to n terms
    else:
        # Start from the third term and generate up to n terms
        while len(fib_series) < n:
            # Next Fibonacci number is the sum of the last two numbers in the series
            next_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(next_fib)
        return fib_series
