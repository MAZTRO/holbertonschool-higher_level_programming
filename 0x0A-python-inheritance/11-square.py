#!/usr/bin/python3
"""
    Write a class BaseGeometry:
    that add Public instance method:
    that validates value
"""


class BaseGeometry:
    """ This is a class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int or value is None):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


"""
    Write a class Rectangle that inherits from BaseGeometry
    Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
"""


class Rectangle(BaseGeometry):
    """ This is a class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


"""
    Write a class Square that inherits from Rectangle
    the area() method must be implemented
    str() should return, the square description: [Square] <width>/<height>
"""


class Square(Rectangle):
    """ This is a class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
