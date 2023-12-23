def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome!")
else:
    print(f"{input_string} is not a palindrome.")
