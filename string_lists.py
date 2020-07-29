# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: string_lists.py
Program asks the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

def main():

    while True:

        # Ask the user to enter a word of any length
        user_input = input("Enter a word of any length: ")

        # Pass the user input through the palindrome check function
        ans = is_palindrome(user_input)

        # Print result/output
        if ans:
            print("Yes")
        else:
            print("No")


# Check to see if the user word is a palindrome or not
def is_palindrome(str):
    
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

    
if __name__ == '__main__':
    main()