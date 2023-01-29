#write a python code for palindrome
def is_palindrome(input_string):
    input_string = input_string.lower()
    return input_string == input_string[::-1]
print(is_palindrome(""))