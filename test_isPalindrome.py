def test_isPalindrome():
    assert isPalindrome("madam") == True
    assert isPalindrome("12321") == True
    assert isPalindrome("hello") == False
    assert isPalindrome("") == True
    assert isPalindrome("123456") == False

test_isPalindrome()