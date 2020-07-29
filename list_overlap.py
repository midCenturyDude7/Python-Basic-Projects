# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: list_overlap.py
Program returns a list that contains only the elements that are common between the lists; and one
list is different in length (number of elements) than the other.
"""

def main():
    
    # Create two separate lists
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Create empty list to store common elements of equal value from two different lists, a and b
    same_elements = []

    # Loop through list a and list b and locate equal/common elements and add to new list, same_elements
    for i in a:
        if i in b:
            if i not in same_elements:
                same_elements.append(i)

    # Print result
    print(same_elements)

if __name__ == '__main__':
    main()