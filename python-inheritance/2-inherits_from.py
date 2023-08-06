"""Only sub class of

def inherits_from: 
    True if the object is an instance of 
    a class that inherited (directly or indirectly) 
    from the specified class ; otherwise False.

    parameters
    
    ----------

    abj(any) -> object of the class

    a_class -> a specified class


"""

def inherits_from(obj, a_class):
    """ Function definition

    parameters
    
    ----------

    abj(any) -> object of the class

    a_class -> a specified class

    * Returns 

    ---------
    True if the object is an instance of 
    a class that inherited (directly or indirectly) 
    from the specified class ; otherwise False.

    ----------
    """


    return issubclass(type(obj), a_class)
