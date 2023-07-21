#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE/
# get the last digit of the number
last_digit = abs(number) % 10

# get the polarity of the number 
polarity = -1 if number < 0 else 1

# determine the message
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# print the complete message
print(f"Last digit of {polarity*number:d} is {polarity*last_digit} {message}")

