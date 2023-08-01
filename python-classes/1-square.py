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
        """
        method to set the size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")



#     def set_size(self, size=0):
#         self.__size = size
#         if type(size) != int:
#             raise TypeError("size must be an integer")
#         elif size<0:
#             raise ValueError("size must be >= 0")
#     def get_size(self):
#         return self.__size
# h = 54
# print(type(4545))