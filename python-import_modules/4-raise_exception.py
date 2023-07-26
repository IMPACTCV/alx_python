def raise_exception():
    try:
        x = 1 + "string"
    except TypeError:
        print("Exception raised")
        raise

