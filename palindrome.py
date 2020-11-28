"""
Filename: palindrome.py
Program will check to see if a string is a palindrome
"""

def is_palindrome(input_string):
    #Two strings will be created for the sake of comparison
    new_string = input_string.replace(" ", "").lower()
    reverse_string = input_string.replace(" ", "").lower()[::-1]

    if new_string == reverse_string:
        return True
    return False