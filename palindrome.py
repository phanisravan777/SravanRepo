def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def test_is_palindrome():
    input_data = [['madam'], ['hello'], ['level'], ['radar'], ['python']]
    expected_output = [[True, False, True, True, False]]
    for i in range(len(input_data)):
        assert isPalindrome(input_data[i][0]) == expected_output[0][i], f'Test case {i+1} failed'

test_is_palindrome()