#!/usr/bin/python3
"""function that adds 2 integers.

    Returns an integer: the addition of a and b.
"""


def add_integer(a, b=98):
    """Function to add:
        Args:
            a (int): A viariable
            b (int): A contant
        Returns:
            (int): the addition of two integers
    """

    if ((type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")
    elif ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a + b))
