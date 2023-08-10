"""
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
"""

from base import Base

"""
define my class
"""

class Rectangle(Base):
    """
define my class
"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """
        models/rectangle.py
        Private instance attributes

        Arguments:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle.
            y: The y-coordinate of the rectangle.
            id: The ID of the rectangle.

        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    """
    defining getter and setter for every private attribute
    """

    @property
    def width(self):
        """Get the width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """set the width"""
        self.__width = width

    @property
    def height(self):
        """get the height"""
        return self.__height
    
    @height.setter
    def width(self, height):
        """set the height"""
        self.__height = height

    @property
    def x(self):
        """get x-coordinate of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """set the x-coordinate of the rectangle"""
        self.__x = x

    @property
    def y(self):
        """get the y-coordinate of the rectangle"""
        return self.__y
    
    @y.setter
    def width(self, y):
        """set the y-coordinate of the rectangle"""
        self.__y = y
        