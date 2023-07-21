def fibonacci_sequence(n):
    if n <= 0:  # Edge case for n less than or equal to 0
        return []
    elif n == 1:  # Edge case for n equal to 1
        return [0]
    else:  # General case for n greater than 1
        fibonacci = [0, 1]  # Initialize the fibonacci list with the first two numbers
        while len(fibonacci) < n:  # Loop until the fibonacci list has n elements
            next_fibonacci = fibonacci[-1] + fibonacci[-2]  # Compute the next Fibonacci number
            fibonacci.append(next_fibonacci)  # Add the next Fibonacci number to the list
        return fibonacci


fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence
