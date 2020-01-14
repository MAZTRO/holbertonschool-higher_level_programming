#!/usr/bin/python3
"""function that adds 2 integers.
    Returns an integer: the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def say_my_name(first_name, last_name=""):
    """
        a and b must be first casted to integers if they are float
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
