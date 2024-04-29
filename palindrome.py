# Function to check if a string is a palindrome
def is_palindrome(s):
    # Normalize the string by converting it to lowercase and removing non-alphanumeric characters
    normalized_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string reads the same forwards and backwards
    return normalized_string == normalized_string[::-1]
