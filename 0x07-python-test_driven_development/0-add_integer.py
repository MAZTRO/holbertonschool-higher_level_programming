#!/usr/bin/python3
"""function that adds 2 integers.
    Returns an integer: the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def add_integer(a, b=98):
    """
        a and b must be first casted to integers if they are float
    """
    if ((type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")
    elif ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a + b))
