# data comes from Johns Hopkins Univeristy. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# you can find data beyond cumulative cases there!

"""
File: data_science_pandas.py
This program pulls the data from the italy.txt file and displays it in a Pandas
dataframe.
"""

import pandas as pd
import matplotlib.pyplot as plt

ITALY_PATH = 'italy.txt'

# This directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'

def main():
    text_plot()
    pandas_demo()


def text_plot():
    # Open the file and read it into a list
    with open(ITALY_PATH) as f:
        italy_data = f.readlines()

    # Scale the data down to fit on screen - max of about 100
    for i in range(len(italy_data)):
        italy_data[i] = float(italy_data[i])/2000

    # Plot the data
    for value in italy_data:
        for i in range(int(value)):
            print(' ', end='')
        print('o')


def pandas_demo():
    # Read the data into a dataframe
    df = pd.read_csv(ITALY_PATH, names=['cases'])

    # Calculate difference from one day to the next
    df['new_cases'] = df['cases'] - df['cases'].shift(1)

    # Plot! Second line required to make plot stay onscreen
    df['new_cases'].plot()
    plt.show()


if __name__ == '__main__':
    main()