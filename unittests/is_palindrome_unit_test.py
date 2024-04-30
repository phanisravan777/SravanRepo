import unittest

from testPythonCode.3127ace8_69e4_4094_b8d2_5f0591600d29 import is_palindrome

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
        self.assertTrue(is_palindrome('Aa'))  # Case insensitive
        self.assertFalse(is_palindrome('AB'))  # Two different characters

if __name__ == '__main__':
    unittest.main()