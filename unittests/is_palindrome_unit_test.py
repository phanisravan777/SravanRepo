import unittest
from d0b0c971_1d95_4582_b105_8de9ef83f3a2 import is_palindrome

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


if __name__ == '__main__':
    unittest.main()