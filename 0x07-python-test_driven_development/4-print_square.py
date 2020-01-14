#!/usr/bin/python3
"""function that print a square with "#" character.

    Returns: Nothing, only print
"""


def print_square(size):
    """Function that print a square:
        Args:
            size (int): The size of the square.
        Returns:
            Nothing, only print
    """

    if (type(size) is float):
        raise TypeError("size must be an integer")
    elif (type(size) is not int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        if (size == 0):
            print("\n", end='')
        else:
            for count in range(size):
                print("#" * size)
