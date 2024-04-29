# Test Cases for is_palindrome

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True
    
# Additional Edge Cases

def test_is_palindrome_edge():
    assert is_palindrome("") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("A Santa at NASA") == True