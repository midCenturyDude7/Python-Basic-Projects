# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: character_input.py
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.
"""

def main ():
    
    while True:
        
        # Ask the user to enter their name 
        user_name = input("Enter your name: ")

        # Ask the user to enter their age
        user_age = input("Enter your age: ")
        
        # Calculate when user will turn 100
        ans = (100 - int(user_age)) + 2020

        # Print result to console
        print("Hello " + user_name + ", you will turn 100 in the year " + str(ans))


if __name__ == '__main__':
    main()