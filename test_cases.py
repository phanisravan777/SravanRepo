# Test Cases for isPalindrome function

def test_isPalindrome():
    assert isPalindrome('madam') == 'The string is a palindrome.'
    assert isPalindrome('hello') == 'The string is not a palindrome.'
    assert isPalindrome('12321') == 'The string is a palindrome.'
    assert isPalindrome('racecar') == 'The string is a palindrome.'
    assert isPalindrome('python') == 'The string is not a palindrome.'