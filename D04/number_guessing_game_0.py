# Create a file called number_guessing_game_0.py
# Using the random module the computer "thinks" about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
# The game ends after just one guess.

import random

num = random.randint(0, 20)
user_num = int(input("Enter a number between 0 and 20: "))
if num == user_num:
    "You are right! This is the number"
else:
    "You are wrong!"