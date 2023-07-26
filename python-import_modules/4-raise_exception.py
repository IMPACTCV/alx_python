def raise_exception():
    x = "string"  # This is a string object
    if type(x) != int:
        raise TypeError  # Raise TypeError if x is not of type int


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

