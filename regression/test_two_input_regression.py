import unittest

from a4ac7950_b863_40c8_9a9f_0d09986ae282 import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            Fibonacci(-1)

    def test_zero_input(self):
        self.assertEqual(Fibonacci(0), 0)

    def test_one_input(self):
        self.assertEqual(Fibonacci(1), 1)

    def test_two_input(self):
        self.assertEqual(Fibonacci(2), 1)

    def test_large_input(self):
        self.assertEqual(Fibonacci(10), 55)

    def test_random_input(self):
        self.assertEqual(Fibonacci(6), 8)

if __name__ == '__main__':
    unittest.main()