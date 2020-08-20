# Taken from Practice Python - Beginner Python Exercises
# Ref url: http://www.practicepython.org/

"""
Filename: roshambo.py
Program is a two-player Rock-Paper-Scissors game
"""

# Constants
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

def main():

    # Introduction
    print("Hello! Welcome to a quick game of Rock-Paper-Scissors!")
    print("Follow the prompt and enter your 'weapon' of choice...")
    
    while True:
        # Player input
        player_one = input("Player one: ")
        player_two = input("Player two: ")

        # Assign weights to Rock, Paper and Scissors
        if player_one == player_two:
            print("You both entered the same weapon! Try again!")
        elif player_one == ROCK and player_two == SCISSORS:
            print("Player One is the winner!")
            break
        elif player_one == ROCK and player_two == PAPER:
            print("Player Two is the winner!")
            break
        elif player_one == PAPER and player_two == ROCK:
            print("Player One is the winner!")
        elif player_one == PAPER and player_two == SCISSORS:
            print("Player Two is the winner!")
        elif player_one == SCISSORS and player_two == ROCK:
            print("Player Two is the winner!")
        elif player_one == SCISSORS and player_two == PAPER:
            print("Player One is the winner!")
        else:
            print("That's not an option. You must enter, 'Rock', 'Paper' or 'Scissors'.") 
            print("Try Again!")

def play_again():
    play_it = "Y"
    end_game = "N"
    user_input = input("Would you like to play again? Y/N: ")
    
    if user_input == end_game:
        print("Thanks for playing!")
    else:
        print("Okay, let's play again!")


if __name__ == '__main__':
    main()