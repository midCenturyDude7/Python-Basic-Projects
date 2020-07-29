# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: roshambo.py
Program is a two-player Rock-Paper-Scissors game
"""

def main():

    # Introduction
    print("Hello! Welcome to a quick game of Rock-Paper-Scissors!")
    print("Follow the prompt and enter your 'weapon' of choice...")
    
    while True:
        # Player input
        player_one = input("Player one: ")
        player_two = input("Player two: ")

        # Assign values to strings
        rock = ["Rock", "rock"]
        paper = ["Paper", 'paper']
        scissors = ["Scissors", "scissors"]

        # Assign weights to Rock, Paper and Scissors
        if player_one == rock or paper or scissors and player_two == rock or paper or scissors:
            if player_one == player_two:
                print("Try again!")
            else: print("That's not an option. You must enter, 'Rock', 'Paper' or 'Scissors'.")




if __name__ == '__main__':
    main()