# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: list_comprehension.py
Program in one line of code that takes a list of variables/numbers and prints only 
the even numbers
"""

def main():

    # List of numbers
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    # Create a list and append the list via list comprehension that checks for odd/even numbers
    # Result: [4, 16, 36, 64, 100]
    even_numbers =  [item for item in a if item % 2 == 0]

    # Try a different approach without a conditional statement
    # Result: [False, True, False, True, False, True, False, True, False, True]
    even_numbers_version_two = [item % 2 == 0 for item in a]   

    # Print result
    print(even_numbers)
    print(even_numbers_version_two)


if __name__ == '__main__':
    main()