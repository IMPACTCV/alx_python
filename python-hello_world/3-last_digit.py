#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE/
last = str(number)[-1]
if int(last) > 5:
    print("last digit of", number, "is", last, "and is greater than 5")
elif int(last) < 6 and int(last) != 0:
    print("last digit of", number, "is", last, "and is less than 6 and not 0")
else:
    print("last digit of", number, "is", last, "and is 0")
