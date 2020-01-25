#!/usr/bin/python3
from models.base import Base
import json


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.verify(width=width, height=height, x=x, y=y, id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def verify(self, **kwargs):
        for key, val in kwargs.items():
            if (key == "width"):
                if (type(val) is not int or val is None):
                    raise TypeError("width must be an integer")
                if (val <= 0):
                    raise ValueError("width must be >= 0")
            if (key == "height"):
                if (type(val) is not int or val is None):
                    raise TypeError("height must be an integer")
                if (val <= 0):
                    raise ValueError("height must be >= 0")
            if (key == "x"):
                if (type(val) is not int):
                    raise TypeError("x must be an integer")
                if (val < 0):
                    raise ValueError("x must be >= 0")
            if (key == "y"):
                if (type(val) is not int):
                    raise TypeError("y must be an integer")
                if (val < 0):
                    raise ValueError("y must be >= 0")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.verify(width=value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.verify(height=value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.verify(x=value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.verify(y=value)
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        if (self.__y > 0):
            print("\n" * (self.__y - 1))
        for count in range(self.__height):
            count += 1
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - \
{}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        if (len(args) != 0):
            my_list = ["id", "width", "height", "x", "y"]
            cnt = 0
            for atr in args:
                setattr(self, my_list[cnt], atr)
                cnt += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        dic = {}
        my_list = ["id", "width", "height", "x", "y"]
        for idx in my_list:
            dic[idx] = getattr(self, idx)
        return (dic)
