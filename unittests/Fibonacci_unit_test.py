import unittest

from Fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    # Basic Test Cases
    def test_Fibonacci_zero(self):
        self.assertEqual(Fibonacci(0), 0)

    def test_Fibonacci_one(self):
        self.assertEqual(Fibonacci(1), 1)

    def test_Fibonacci_two(self):
        self.assertEqual(Fibonacci(2), 1)

    def test_Fibonacci_three(self):
        self.assertEqual(Fibonacci(3), 2)

    # Edge Test Cases
    def test_Fibonacci_negative(self):
        with self.assertRaises(ValueError):
            Fibonacci(-1)

    def test_Fibonacci_large(self):
        self.assertEqual(Fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()