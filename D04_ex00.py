#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
##########################################################################
# Imports
import random

# Body


def random_guess_game():
    x = random.randint(1, 25)
    count = 0
    while count < 5:
        user_input = ''
        while user_input == '':
            try:
                user_input = int(
                    input("Please guess my number between 1 and 25: "))
                if 1 <= user_input < x:
                    print("Too low, you have " +
                          str(4 - count) + " attempts left")
                    count += 1
                elif x < user_input <= 25:
                    print("Too high, you have " +
                          str(4 - count) + " attempts left")
                    count += 1
                elif user_input == x:
                    print('You guessed correctly!')
                    count = 7
                else:
                    print("That integer is not between 1 and 25.\nYou have " +
                          str(4 - count) + " attempts left")
                    count += 1
            except:
                count += 1
                if count == 5:
                    print('That was not a valid input.')
                    break
                else:
                    print("That was not a valid input. Please insert an integer between 1 and 25.\nYou have " +
                          str(5 - count) + " attempts left")
    if count == 5:
        print("Sorry, you ran out of attempts")


##########################################################################
def main():
    return random_guess_game()


if __name__ == '__main__':
    main()
