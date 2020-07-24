# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: list_less_than_ten.py
(1) Application prints out all the elements of the list that are less than 5;
(2) Makes a new list that has all the elements less than 5 from the main list in it and prints out this new list; and,
(3) Makes a new list that has all the elements greater than or equal to 5 from the main list in it and prints out this new list.
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
    
    # Print results
    print(lesser_list)
    print(bigger_list)

    # List comprehension for the for loop above
    comp_lesser_list = [i for i in main_list if i < 5]
    comp_bigger_list = [i for i in main_list if i >= 5]

     # Print results
    print(comp_lesser_list)
    print(comp_bigger_list)


if __name__ == '__main__':
    main()