""""
class: defined class call square 
"""
class Square:
    """
    medoth to get the class
    """
    def __init__(self, size=0):
        """
    private instance attribute: size
    
    """
        self.__size = size

        if type(size) != int and type(size) == str:
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        
    """
    Pulici instance method: def area(self):
    tha returns the current square area
    """

    def area(self):
        return self.__size ** 2
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value
