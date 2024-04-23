# Basic Test Cases
def test_is_palindrome_basic():
    assert isPalindrome('madam') == True
    assert isPalindrome('hello') == False
    assert isPalindrome('level') == True
    assert isPalindrome('radar') == True
    assert isPalindrome('python') == False

# Edge Test Cases
def test_is_palindrome_edge():
    assert isPalindrome('') == True
    assert isPalindrome('a') == True
    assert isPalindrome('ab') == False
    assert isPalindrome('racecar') == True
    assert isPalindrome('12321') == True