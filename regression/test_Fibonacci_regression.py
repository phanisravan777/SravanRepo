import unittest
from ccd60db1_27e1_4ce6_b180_c8bf2be3ff5b import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(Fibonacci(0), 0)
        self.assertEqual(Fibonacci(1), 1)
        self.assertEqual(Fibonacci(2), 1)
        self.assertEqual(Fibonacci(3), 2)
        self.assertEqual(Fibonacci(10), 55)
        self.assertEqual(Fibonacci(-1), 'Incorrect input')
        self.assertEqual(Fibonacci(30), 832040)

if __name__ == '__main__':
    unittest.main()