#!/usr/bin/python3
class Square:
    """ Class Square to calculate an area.
    Define a empty class

    Attributes:
        __size (int): Value of the an edge of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        if (type(size and position[0] and position[1]) is not int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
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
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0] and value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        if self.__size <= 0:
            print("\n", end='')
        else:
            for count_1 in range(self.__position[1]):
                print()
            for count_4 in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
