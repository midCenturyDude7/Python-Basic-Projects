# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: list_less_than_ten.py
Application prints out all the elements of the list that are less than 5.
"""

def main():
    
    # List with ten numbers
    main_list = [1, 1, 2, 3, 4, 5, 25, 45, 98, 101]
    
    # Empty list to capture all numbers from main_list less than five
    lesser_list = []

    # Empty list to capture all numbers from main_list greater than or equal to five
    bigger_list = []

    # Loop throught main_list
    for i in main_list:

        # Check to see if number is less than five or not and include in appropriate list - lesser or bigger
        if i < 5:
            lesser_list.append(i)
        else:
            bigger_list.append(i)
    
    # Print lists
    print(lesser_list)
    print(bigger_list)


if __name__ == '__main__':
    main()