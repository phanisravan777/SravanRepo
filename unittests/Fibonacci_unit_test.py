import unittest
from ccd60db1_27e1_4ce6_b180_c8bf2be3ff5b import Fibonacci
class TestFibonacci(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(Fibonacci(-1), 'Incorrect input')
    def test_zero_input(self):
        self.assertEqual(Fibonacci(0), 0)
    def test_one_input(self):
        self.assertEqual(Fibonacci(1), 1)
    def test_two_input(self):
        self.assertEqual(Fibonacci(2), 1)
    def test_three_input(self):
        self.assertEqual(Fibonacci(3), 2)
    def test_large_input(self):
        self.assertEqual(Fibonacci(10), 55)
if __name__ == '__main__':
    unittest.main()