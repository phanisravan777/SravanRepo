#To Check given string is palindrome or not
#This below code determines whether given string is palindrome or not.
def isPalindrome(string): 
    if (string == string[::-1]) : 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 
