#!/usr/bin/python3
class Square:
    """ Class Square to calculate an area.
    Define a empty class

    Attributes:
        __size (int): Value of the an edge of the square.
    """
    def __init__(self, size=0):
        """ __init__method to initialize the atributes.
        Args:
            size (int): Size of the edge of the square.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
