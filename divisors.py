# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: divisors.py
Program asks the user for a number and then prints out a list of all the divisors of that number.
"""

def main():

    # Ask user to enter a number
    user_num = int(input("Enter a number to divide: "))

    # Create a range from 1 to the number the user enters
    list_range = list(range(1, user_num+1))

    # Create empty list to capture all divisors of user number
    divisor_list = []

    # Loop through the list_range
    for elem in list_range:
        if user_num % elem == 0:
            divisor_list.append(elem)

    # Print result
    print(divisor_list)


if __name__ == '__main__':
    main()