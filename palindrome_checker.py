def isPalindrome(string):
    if (string == string[::-1]):
        return 'The string is a palindrome.'
    else:
        return 'The string is not a palindrome.'

def test_is_palindrome():
    input_data = [['madam'], ['hello'], ['12321'], ['racecar'], ['python']]
    expected_output = [['The string is a palindrome.'], ['The string is not a palindrome.'], ['The string is a palindrome.'], ['The string is a palindrome.'], ['The string is not a palindrome.']]
    for i in range(len(input_data)):
        assert isPalindrome(input_data[i][0]) == expected_output[i][0], f'Test Case {i+1} Failed'
    print('All test cases passed successfully!')

test_is_palindrome()