# Create a file called number_guessing_game_6.py
# Let the user play several games.
# Pressing 'n' will skip this game and start a new one. Generates a new number to guess.

import random

# Start with a random number between 0 and 20
num = random.randint(0, 20)
debug = False
move_mode = False
new_move = False

print("Guess the number between 0 and 20. Type 'x' to quit, 'd' to toggle debug mode, 'm' to toggle move mode and 'n' to skip this turn")

while True:
    if debug:
        print(f"[DEBUG] Current number: {num}")
    
    user_input = input("Your guess: ").strip().lower()
    if new_move:
        num = random.randint(0, 20)

    if user_input == 'x':
        print("Exiting the game.")
        break
    elif user_input == 'n':
        new_move = True
        continue
    elif user_input == 'd':
        debug = not debug
        print(f"Debug mode {'ON' if debug else 'OFF'}.")
        continue
    elif user_input == 'm':
        move_mode = not move_mode
        print(f"Move mode {'ON' if move_mode else 'OFF'}.")
        continue
    elif not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    if guess == num:
        print("You nailed it!")
        continue
    else:
        print("Try again.")

    if move_mode:
        # Modify the number by -2, -1, 0, 1, or 2
        num += random.choice([-2, -1, 0, 1, 2])
        # Keep the number in a reasonable range (e.g., 0–20)
        num = max(0, min(20, num))