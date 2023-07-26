def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

    


a = 12
b = 2
if __name__ == "__main__":
    print("{:d} / {:d} = {}".format(a, b, safe_print_division(a, b)))
   
