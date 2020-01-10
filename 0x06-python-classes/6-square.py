#!/usr/bin/python3
class Square:
    """ Class Square to calculate an area.
    Define a empty class

    Attributes:
        __size (int): Value of the an edge of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__method to initialize the atributes.
        Args:
            size (int): Size of the edge of the square.
        """
        if (type(size and position[0] and position[1]) is not int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """ area method to power the atributes.
        Args:
            Nothing.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size method to initialize the atributes.
        Args:
            size (int): Size of the edge of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value[0] and value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise ValueError('position must be >= 0')
        else:
            self.__position = value

    def my_print(self):
        if self.__size <= 0:
            print("\n", end='')
        else:
            for count in range(self.__size):
                print(" ", end='' * self.__position[0])
                print("#" * self.__size)
