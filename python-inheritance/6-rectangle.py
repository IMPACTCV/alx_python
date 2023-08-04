"""Rectangle

--------

This script requirea  Python
environment install where you are running this script in.

write an empty class

"""


class BaseGeometry:
    """
    A class defined

    -------

    def area(self): --> methods to return exception

    Raise:
    Exception with meassage
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    """
    Public:

    -------

    def integer_validator(self, name, value): --> validates value
    """

    def integer_validator(self, name: str , value):
        self.name = name
        if type(self.value) != int:
            raise TypeError("<name> must be an integer")
        elif self.value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value


class Rectangle(BaseGeometry):
    """
    class Reactangle -->

    Inherits from BaseGeomerty

    --------
    Parameters
    ----------

    width: the width of the rectangle

    height: the height of the rectancle

    ----------
    
    returs --->
    width and height must be positive 
    integers, validated by integer_validator() function
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
        super().__init__()


