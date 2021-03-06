#!/usr/bin/python3
"""
    Class to calculate a Rectangule.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ("")
        else:
            matrix_a = (("#" * self.__width) + "\n") * (self.__height - 1)
            matrix_b = ("#" * self.__width) * (1)
            return (matrix_a + matrix_b)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
