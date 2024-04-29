def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fib_list.append(b)
        return fib_list
