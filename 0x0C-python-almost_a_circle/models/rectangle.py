#!/usr/bin/python3
""" Class Rectangle """


from models.base import Base
import json


class Rectangle(Base):
    """ Init """
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.verify(width=width, height=height, x=x, y=y, id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def verify(self, my_dict):
        """ Verify """
        for key, val in my_dict.items():
            if (val is not int):
                raise TypeError("{} must be an integer".format(key))
            elif (val <= 0 and key != "x" and key != "y"):
                raise ValueError("{} must be > 0".format(key))
            elif (val < 0 and key != "width" and key != "height"):
                raise ValueError("{} must be > 0".format(key))

    @property
    def width(self):
        """ Set_width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set_ width """
        self.verify(width=value)
        self.__width = value

    @property
    def height(self):
        """ Set_heigth """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set_heigth """
        self.verify(height=value)
        self.__height = value

    @property
    def x(self):
        """ Set_x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Set_x """
        self.verify(x=value)
        self.__x = value

    @property
    def y(self):
        """ Set_y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Set_y """
        self.verify(y=value)
        self.__y = value

    def area(self):
        """ Return area """
        return (self.__width * self.__height)

    def display(self):
        """ Print area """
        if (self.__y > 0):
            print("\n" * (self.__y - 1))
        for count in range(self.__height):
            count += 1
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - \
{}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Update data """
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
        """ Convert area """
        dic = {}
        my_list = ["id", "width", "height", "x", "y"]
        for idx in my_list:
            dic[idx] = getattr(self, idx)
        return (dic)
