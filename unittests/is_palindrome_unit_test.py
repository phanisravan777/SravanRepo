import unittest
from ccd60db1_27e1_4ce6_b180_c8bf2be3ff5b import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    # Basic Test Cases
    def test_basic(self):
        self.assertEqual(is_palindrome('racecar'), True)
        self.assertEqual(is_palindrome('hello'), False)
        self.assertEqual(is_palindrome('A man, a plan, a canal: Panama'), True)

    # Edge Test Cases
    def test_edge(self):
        self.assertEqual(is_palindrome(''), True)
        self.assertEqual(is_palindrome('A'), True)
        self.assertEqual(is_palindrome('AB'), False)
        self.assertEqual(is_palindrome('Aa'), True)
        self.assertEqual(is_palindrome('12321'), True)
        self.assertEqual(is_palindrome('12345'), False)

if __name__ == '__main__':
    unittest.main()