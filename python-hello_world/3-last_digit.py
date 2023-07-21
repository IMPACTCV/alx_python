#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE/
# Compute the last digit of the number (using absolute value to handle negative numbers)
last_digit = abs(number) % 10

# Determine the corresponding text based on the last digit
if last_digit > 5:
    text = "and is greater than 5"
elif last_digit == 0:
    text = "and is 0"
else:
    text = "and is less than 6 and not 0"

# Output the full sentence
print("Last digit of {} is {} {}".format(number, last_digit, text))

