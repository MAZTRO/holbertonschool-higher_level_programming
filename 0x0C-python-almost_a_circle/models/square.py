#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({})\
 {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if (len(args) != 0):
            my_list = ["id", "size", "x", "y"]
            cnt = 0
            for atr in args:
                setattr(self, my_list[cnt], atr)
                cnt += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        atr = {"id": self.id, "size": self.size, "x": self.__x, "y": self.__y}
        return (atr)
