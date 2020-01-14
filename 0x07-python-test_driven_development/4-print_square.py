#!/usr/bin/python3
"""function that adds 2 integers.
    Returns an integer: the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def print_square(size):
    """
        a and b must be first casted to integers if they are float
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
