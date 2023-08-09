"""
create a class

"""

class Base:
    """
    class defined
    """

    # define a private attribut

    __nb_objects = 0

    # constructor
    def __init__(self, id=None):
        if id is not None:
            self.id = self.__nb_objects
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

