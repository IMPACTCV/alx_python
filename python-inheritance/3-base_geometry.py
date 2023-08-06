"""Geometry module

--------

This script requirea  Python
environment install where you are running this script in.

write an empty class

"""

class BaseGeometry:
    """
    A class defined
    """
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [x for x in attributes if x != "__init_subclass__"]
        return new_attribute_list
