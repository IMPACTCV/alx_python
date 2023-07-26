def raise_exception():
    my_var = 123
    my_var += "abc"  # This raises a TypeError


try:
    raise_exception()
except TypeError as te:
    print("")

