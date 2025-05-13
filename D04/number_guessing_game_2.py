# Create a file called number_guessing_game_2.py
# If the user hits 'x', we leave the game without guessing the number.

import random

num = random.randint(0, 20)
print("You Enter a number between 0 and 20. Press x to quit ")

while True:
    user_num = input("Your guess: ")
    
    if user_num.lower() == 'x':
        print("Exit game.")
        break
    
    if not user_num.isdigit():
        print("Please enter a valid number.")
        continue

    user_num = int(user_num)

    if user_num != num:
        print("Try again.")
        continue  
    else:
       print("You nailed it!")
       break