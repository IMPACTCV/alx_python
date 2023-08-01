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

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        
    """
    Publici instance method: def area(self):
    tha returns the current square area
    """

    def area(self):
        return self.__size ** 2
    
    """
    define the getter method
    """
    @property
    def size(self):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size<0:
            raise ValueError("size must be >= 0")
        return self.__size
    """
    define the setter method
    """
    @size.setter
    def size(self, value):
        self.__size = value

    """
    Publici instance method: def my_print(self):
    tha returns the current square area
    """
    def my_print(self):
        for i in range(self.__size):
            if self.__size != 0:
                print("#" * self.__size)
            else:
                print(" ")

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")