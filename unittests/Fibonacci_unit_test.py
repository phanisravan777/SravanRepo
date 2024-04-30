import unittest

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(Fibonacci(0), 0)
        self.assertEqual(Fibonacci(1), 1)
        self.assertEqual(Fibonacci(2), 1)
        self.assertEqual(Fibonacci(3), 2)
        self.assertEqual(Fibonacci(4), 3)
        self.assertEqual(Fibonacci(5), 5)

if __name__ == '__main__':
    unittest.main()