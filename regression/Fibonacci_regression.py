class TestFibonacci(unittest.TestCase):
    
    def test_Fibonacci(self):
        self.assertEqual(Fibonacci(0), 0)
        self.assertEqual(Fibonacci(1), 1)
        self.assertEqual(Fibonacci(2), 1)
        self.assertEqual(Fibonacci(3), 2)
        self.assertEqual(Fibonacci(4), 3)
        self.assertEqual(Fibonacci(5), 5)
        self.assertEqual(Fibonacci(6), 8)
        self.assertEqual(Fibonacci(7), 13)
        self.assertEqual(Fibonacci(8), 21)
        self.assertEqual(Fibonacci(9), 34)

if __name__ == '__main__':
    unittest.main()