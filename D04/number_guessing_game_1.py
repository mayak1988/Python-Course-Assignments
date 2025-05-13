# Create a file called number_guessing_game_1.py
# The user can guess several times. The game ends when the user guessed the right number.
import random

num = random.randint(0, 20)
user_num = int(input("You Enter a number between 0 and 20: "))
while num != user_num:
    user_num = int(input("You are wrong! Enter a number between 0 and 20: "))
else:
    "You got it!"