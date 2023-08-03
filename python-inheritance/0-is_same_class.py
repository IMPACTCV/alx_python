"""Exact same object

This script allow the user to cheack if
a particular object is an instance of a class

This script requirea  Python
environment install where you are running this script in.

* isinstance - is_same_class - returns True if the object 
is exactly an instance of the specified class ; otherwise False
"""

def is_same_class(obj, a_class):
    """ Get and print True or False 

    parameters
    
    ----------
    obj : attribut
        the name of the object
    a_class: class
        the class name
    
    Returns

    -------
    Bool - specifing if the object is an the instance of that class

    """
    
    if type(obj) == bool and a_class == int:
    
         return False
    elif a_class == object:
         return False
    # elif type(obj) == int or type(obj) == list or type(obj) == object:

    #     return isinstance(obj, a_class)
    # else:
    #     print(type(a), type(object))
    # if type(obj) == int:
    #     return 
    return isinstance(obj, a_class)
    
# c = is_same_class(a, object)

a = True
print(is_same_class([1,2,3], object))

