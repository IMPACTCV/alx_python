"""Improve Geometry

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
    def __dir__(self):
        """
        define the function:

    parameters-->
    self -> no parameters
        """
        attributes = super().__dir__()
        new_attribute_list = [x for x in attributes if x != "__init_subclass__"]
        return new_attribute_list
    
    def area(self):
        """
        Function to raise exception
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

