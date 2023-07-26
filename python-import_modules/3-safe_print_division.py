def safe_print_division(a, b):
    return "{:d} / {:d} = {}".format(a, b, a/b)


a = 12
b = 2
if __name__ == "__main__":
    print(safe_print_division(a, b))
