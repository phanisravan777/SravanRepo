import unittest
from a4ac7950_b863_40c8_9a9f_0d09986ae282 import Fibonacci

class TestFibonacci(unittest.TestCase):

    # Basic Test Cases
    def test_Fibonacci_1(self):
        self.assertEqual(Fibonacci(0), 0)

    def test_Fibonacci_2(self):
        self.assertEqual(Fibonacci(1), 1)

    def test_Fibonacci_3(self):
        self.assertEqual(Fibonacci(2), 1)

    def test_Fibonacci_4(self):
        self.assertEqual(Fibonacci(3), 2)

    def test_Fibonacci_5(self):
        self.assertEqual(Fibonacci(5), 5)

    # Edge Test Cases
    def test_Fibonacci_6(self):
        with self.assertRaises(Exception):
            Fibonacci(-1)

    def test_Fibonacci_7(self):
        self.assertEqual(Fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()