# Data comes from Johns Hopkins University. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# You can find data beyond cumulative cases there!

"""
File: data_science_1.py
Test your code by analysing total confirmed cases over time
Each line in the file represents one day. The first value is confirmed cases on Jan 22nd.
The number of confirmed cases is "cumulative" meaning that it is the total number
of cases up until the current day. It will never go down!
"""

ITALY_PATH = 'italy.txt'

# This directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'

"""
Challenge #1: Load all the values from the file into a list of integers.
"""


def main():
    count = 1                       # Sets day/line counter
    for line in open(ITALY_PATH):   # Open file to read
        line = line.strip()         # Remove new line
        num_italy = line.split()    # Create list of integers
        for num_line in num_italy:  # Print list of integers
            print("Day " + str(count) + ": " + num_line)
            count += 1
    print(ITALY_PATH + " contains " + str(count) + " days of confirmed COVID-19 cases")
    make_the_list()


def make_the_list():
    italy_list = open(ITALY_PATH, 'r')
    list_of_lists = []
    for line in italy_list:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    print(list_of_lists)


if __name__ == '__main__':
    main()