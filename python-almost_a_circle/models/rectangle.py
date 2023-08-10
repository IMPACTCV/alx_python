"""
This model defines the rectangle class which
inherites fron the base class
"""

from models.base import Base

class Rectangle(Base):
    """
define my class Rectangle
"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """Initialize a rectangle.

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

        self.validate_height()
        self.validate_width()
        self.validate_x()
        self.validate_y()

    @property
    def width(self):
        """Get the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        """get the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """get x-coordinate of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """set the x-coordinate of the rectangle"""
        if  not isinstance(value, int):
            raise TypeError("x must be an integer")
        if self.__x<0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y-coordinate of the rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """set the y-coordinate of the rectangle"""
        if  not isinstance(value, int):
            raise TypeError("y must be an integer")
        if self.__y<0:
            raise ValueError("y must be >= 0")
        self.__y = value
       
    """
    Validate attributes task 2
    """
    def validate_width(self):
        """Validate the width"""
        if  not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width<=0:
            raise ValueError(" width must be > 0")
    def validate_height(self):
        """Validate the height"""
        if  not isinstance(self.__height, int):
            raise TypeError("width must be an integer")
        if self.__height<=0:
            raise ValueError(" width must be > 0")
    def validate_x(self):
        """Validate x"""
        if  not isinstance(self.__x, int):
            raise TypeError("y must be an integer")
        if self.__x<0:
            raise ValueError("x must be >= 0")
    def validate_y(self):
        """Validate y"""
        if  not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y<0:
            raise ValueError("y must be >= 0")
        
