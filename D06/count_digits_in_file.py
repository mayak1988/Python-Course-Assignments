# Given the file examples/files/numbers.txt (or a similar file), create a file called count_digits_in_file.py that will count how many times each digit appears? The output will look like this. Just different values.
# Save the results in a file called report.txt.
import numpy as np
import re

with open("numbers.txt", "r") as file:
    content = file.read()
    print(content)


numbers = content.split(' ')
digits = np.zeros(10)
for num in numbers:
    digit_groups = list(re.findall(r'\d', str(num)))
    for digit in digit_groups:
        digits[int(digit)]+=1

# print(digits)


with open("report.txt", "w") as file:
    for i, d in enumerate(digits):
            file.write(f"{i} {int(d)}\n")