import unittest
from testPythonCode.3127ace8_69e4_4094_b8d2_5f0591600d29 import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        # Test case 1: Normal case with palindrome string
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

        # Test case 2: Normal case with non-palindrome string
        self.assertFalse(is_palindrome('Hello World'))

        # Test case 3: Edge case with empty string
        self.assertTrue(is_palindrome(''))

        # Test case 4: Edge case with single character string
        self.assertTrue(is_palindrome('a'))

        # Test case 5: Edge case with string containing only non-alphanumeric characters
        self.assertTrue(is_palindrome('!!!'))

        # Test case 6: Normal case with palindrome string containing numbers
        self.assertTrue(is_palindrome('12321'))

        # Test case 7: Normal case with non-palindrome string containing numbers
        self.assertFalse(is_palindrome('12345'))


if __name__ == '__main__':
    unittest.main()