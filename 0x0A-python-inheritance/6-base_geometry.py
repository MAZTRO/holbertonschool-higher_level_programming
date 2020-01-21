#!/usr/bin/python3
"""
    Add Public instance method:
    that raises an Exception with the message:
    " area() is not implemented "
"""


class BaseGeometry:
    """ This is a class """
    def area(self):
        raise Exception("area() is not implemented")
