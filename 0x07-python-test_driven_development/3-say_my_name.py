#!/usr/bin/python3
"""function that print the first nam and last name.

    Returns: Nothing, only print
"""


def say_my_name(first_name, last_name=""):
    """Function that print a name:
        Args:
            first_name (str): The first string
            last_name (str):: the second string
        Returns:
            Nothing, only print
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
