"""
File: decreasing_numbers/py
This program asks the user to enter a decreasing number each time. Unless the number
is equal to or less than the previous number, the program will end and count the
number of sequences the user entered a number
"""


def main():
    # Initiate program and set the sequence counter to zero
    print("Decreasing number sequence")
    sequence = 0
    last_num = float(input("Enter num: "))
    cur_num = last_num

    # Enter number and start sequence counting
    while cur_num >= last_num:
        sequence += 1
        last_num = cur_num
        cur_num = float(input("Enter num: "))
    print("Thanks for playing!")
    print("Sequence length: " + str(sequence))


if __name__ == '__main__':
    main()