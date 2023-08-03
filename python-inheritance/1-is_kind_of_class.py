"""Same class or inherit from

This script allow the user to cheack if
a particular object is an instance of a class

This script requirea  Python
environment install where you are running this script in.

* isinstance - is_same_class - returns True if the object 
is exactly an instance of the specified class ; otherwise False
"""

def is_kind_of_class(obj, a_class):
    """ Get and print True or False 

    parameters
    
    ----------
    obj : attribut
        the name of the object
    a_class: class
        the class name
    
    Returns

    -------
    Bool - specifing if the object is an the instance of that class or if the object is an instance of a class that inherited from, the specified class
    """

    if isinstance(obj, a_class) or issubclass(obj, a_class):
         return True

    if type(obj) == bool and a_class == int:
    
         return False
    elif a_class == object:
         return False
