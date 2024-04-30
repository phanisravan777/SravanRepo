import unittest
from a4ac7950_b863_40c8_9a9f_0d09986ae282 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        # Test case 1: Normal case with palindrome
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

        # Test case 2: Normal case with non-palindrome
        self.assertFalse(is_palindrome('Hello, World!'))

        # Test case 3: Case with empty string
        self.assertTrue(is_palindrome(''))

        # Test case 4: Case with single character
        self.assertTrue(is_palindrome('a'))

        # Test case 5: Case with special characters only
        self.assertTrue(is_palindrome('!!!'))

        # Test case 6: Case with numbers
        self.assertTrue(is_palindrome('12321'))
        self.assertFalse(is_palindrome('12345'))

        # Test case 7: Case with mixed case palindrome
        self.assertTrue(is_palindrome('Able was I ere I saw Elba'))

        # Test case 8: Case with palindrome containing special characters
        self.assertTrue(is_palindrome('Able, was I... ere I saw: Elba.'))


if __name__ == '__main__':
    unittest.main()