def raise_exception():
    return 
    
try:
    print(raise_exception())
except TypeError as te:
    print("Exception raised")
