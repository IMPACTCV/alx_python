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
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """
    defining getter and setter for every private attribute
    """

    @property
    def get_width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def get_height(self):
        return self.__height
    
    @height.setter
    def width(self, height):
        self.__height = height

    @property
    def get_x(self):
        return self.__x
    
    @x.setter
    def width(self, x):
        self.__x = x

    @property
    def get_y(self):
        return self.__y
    
    @y.setter
    def width(self, y):
        self.__y = y