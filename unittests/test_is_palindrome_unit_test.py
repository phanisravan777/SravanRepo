def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("hello") == False