import random

random_int = random.randint(1, 20)  # includes both 1 and 10
num = int(input('Please choose a number between 1 and 20: '))

if num == random_int:
    print(' You guessed the number')
elif num > random_int:
    print('Your num is bigger than the chosen number')
else:
    print('Your num is smaller than the chosen number')