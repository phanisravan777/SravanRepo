# Regression Test Cases

def isPalindrome(string):
    if (string == string[::-1]):
        return 'The string is a palindrome.'
    else:
        return 'The string is not a palindrome.'

# Test Cases
print(isPalindrome('madam')) # Expected Output: 'The string is a palindrome.'
print(isPalindrome('hello')) # Expected Output: 'The string is not a palindrome.'
print(isPalindrome('level')) # Expected Output: 'The string is a palindrome.'
print(isPalindrome('radar')) # Expected Output: 'The string is a palindrome.'
print(isPalindrome('python')) # Expected Output: 'The string is not a palindrome.'