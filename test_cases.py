# Test Cases for isPalindrome method

# Test Case 1
string = 'madam'
expected_output = 'The string is a palindrome.'
output = isPalindrome(string)
assert output == expected_output, f'Expected: {expected_output}, Got: {output}'

# Test Case 2
string = 'hello'
expected_output = 'The string is not a palindrome.'
output = isPalindrome(string)
assert output == expected_output, f'Expected: {expected_output}, Got: {output}'

# Test Case 3
string = '12321'
expected_output = 'The string is a palindrome.'
output = isPalindrome(string)
assert output == expected_output, f'Expected: {expected_output}, Got: {output}'

# Test Case 4
string = 'racecar'
expected_output = 'The string is a palindrome.'
output = isPalindrome(string)
assert output == expected_output, f'Expected: {expected_output}, Got: {output}'

# Test Case 5
string = 'python'
expected_output = 'The string is not a palindrome.'
output = isPalindrome(string)
assert output == expected_output, f'Expected: {expected_output}, Got: {output}'