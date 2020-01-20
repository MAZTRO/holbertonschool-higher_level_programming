#!/usr/bin/python3
""" Myint, class to inver the functionality of '==' """


class MyInt(int):
    """ My function """

    def __init__(self, value):
        int.__init__(self)
        if (type(value) == int):
            self.__value = value

    def __eq__(self, lol):
        return (self.__value != lol)

    def __ne__(self, lol):
        return (self.__value == lol)
