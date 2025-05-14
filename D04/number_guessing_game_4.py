# <!-- Create a file called number_guessing_game_4.py
# Soon we'll have a level in which the hidden value changes after each guess. In order to make that mode easier to track and debug, first we would like to have a "debug mode".
# If the user presses 'd' the game gets into "debug mode": the system starts to show the current number to guess every time, just before asking the user for new input.
# Pressing 'd' again turns off debug mode. (It is a toggle each press on 'd' changes the value to to the other possible value.) -->


import random

num = random.randint(0, 20)
print("You Enter a number between 0 and 20. Press x to quit ")
debug = False

while True:
    if debug:
        print(f"[DEBUG] The number is: {num}")

    user_num = input("Your guess: ")
    if user_num.lower() == 'd':
        debug = not debug
        continue

    if user_num.lower() == 'x':
        print("Exit game.")
        break
    if user_num.lower() == 's':
        print(f'The number is: {num}')
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