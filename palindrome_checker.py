# function to check string is
# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# Testing the function with provided input
input_data = [['madam', 'racecar', 'hello', 'level', 'radar', 'python', 'mom', 'noon']]
expected_output = [[True, True, False, True, True, False, True, True]]

for i in range(len(input_data[0])):
    assert isPalindrome(input_data[0][i]) == expected_output[0][i], f'Test case {i+1} failed'

print('All test cases passed successfully')