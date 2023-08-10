"""
create the base class class

"""

class Base:
    """
    class defined
    """

    # define a private attribut

    __nb_objects = 0

    # constructor
    def __init__(self, id=None):
        """
        arg:

        id -> this is the id of the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
