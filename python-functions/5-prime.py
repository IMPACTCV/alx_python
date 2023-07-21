def is_prime(number):
    if number <= 1:  # Edge case for numbers less than or equal to 1
        return False
    elif number == 2 or number == 3:  # Edge case for 2 and 3
        return True
    elif number % 2 == 0:  # Other even numbers are not prime
        return False
    else:  # General case for odd numbers greater than 3
        for i in range(3, int(number**0.5) + 1, 2):  # Iterate from 3 to square root of number in steps of 2
            if number % i == 0:  # If number is divisible by i, it is not prime
                return False
        return True
    

is_prime = __import__('5-prime').is_prime
