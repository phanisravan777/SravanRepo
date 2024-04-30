import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome_string(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama'))

    def test_non_palindrome_string(self):
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()