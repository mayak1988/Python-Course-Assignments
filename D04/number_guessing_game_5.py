import random

# Start with a random number between 0 and 20
num = random.randint(0, 20)
debug = False
move_mode = False

print("Guess the number between 0 and 20. Type 'x' to quit, 'd' to toggle debug mode, 'm' to toggle move mode.")

while True:
    if debug:
        print(f"[DEBUG] Current number: {num}")
    
    user_input = input("Your guess: ").strip().lower()

    if user_input == 'x':
        print("Exiting the game.")
        break
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
        break
    else:
        print("Try again.")

    if move_mode:
        num += random.choice([-2, -1, 0, 1, 2])
        num = max(0, min(20, num))