""""
class: defined class call square 
"""
class Square:
    """
    medoth to get the class
    """
    def __init__(self, size):
        """
    private instance attribute: size
    
    """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        elif size == "":
            size = 0

            
