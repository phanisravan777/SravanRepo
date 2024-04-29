# Basic Test Cases
def test_is_palindrome_basic():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

# Edge Test Cases
def test_is_palindrome_edge():
    assert is_palindrome("") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("Able was I, ere I saw Elba") == True