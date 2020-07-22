# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: odd_or_even.py
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
"""

# Ask user to enter a number
user_number = int(input("Enter a number: "))

# Check to see if the number is odd or even
if user_number % 2 == 0:
    print("You entered: " + str(user_number) + ". It is even!")

else:
    print("You entered " + str(user_number) + ". It is odd!")