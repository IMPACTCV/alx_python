def safe_print_division(a, b):
    try:
        return "{:d} / {:d} = {}".format(a, b, a/b)
    except ZeroDivisionError:
        return "Error: Can't divide by zero"
    except ValueError:
        return "Error: Non-numeric input"

    


a = 12
b = 2
if __name__ == "__main__":
    print(safe_print_division(a, b))
