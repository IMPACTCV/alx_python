def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9  # Formula to convert Fahrenheit to Celsius
    return celsius


convert_to_celsius = __import__('2-temperature').convert_to_celsius
