import unittest
from a4ac7950_b863_40c8_9a9f_0d09986ae282 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    # Basic Test Cases
    def test_is_palindrome_basic(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(is_palindrome('hello'))

    # Edge Test Cases
    def test_is_palindrome_edge(self):
        self.assertTrue(is_palindrome(''))  # Empty string
        self.assertTrue(is_palindrome('A'))  # Single character
        self.assertTrue(is_palindrome('Aa'))  # Case insensitivity
        self.assertFalse(is_palindrome('AB'))  # Two different characters
        self.assertTrue(is_palindrome('12321'))  # Numeric palindrome
        self.assertFalse(is_palindrome('12345'))  # Non-palindrome number


if __name__ == '__main__':
    unittest.main()