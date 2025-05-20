# Create a script called count_digits_in_lists.py that given a list of numbers count how many times each digit appears? The output will look like this:


# 0  1
# 1  3
# 2  3
# 3  2
# 4  1
# 5  2
# 6  2
# 7  0
# 8  1
# 9  1

numbers = [1203, 1256, 312456, 98]
import numpy as np
import re
digits = np.zeros(10)
for num in numbers:
    digit_groups = list(re.findall(r'\d', str(num)))
    for digit in digit_groups:
        digits[int(digit)]+=1
# print(digits)
[print(i, int(d)) for i, d in enumerate(digits)]