import unittest
from d0b0c971_1d95_4582_b105_8de9ef83f3a2 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('A'))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('Python'))

    def test_is_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome('Able , was I saw Elba'))
        self.assertTrue(is_palindrome('Madam, in Eden, I’m Adam'))
        self.assertFalse(is_palindrome('Hello, World!'))

    def test_is_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertTrue(is_palindrome('1a2b2a1'))
        self.assertFalse(is_palindrome('12345'))


if __name__ == '__main__':
    unittest.main()