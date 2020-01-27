#!/usr/bin/python3
""" Square file"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return STR """
        return ("[Square] ({})\
 {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update """
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
        """ To dictionary """
        dic = {}
        my_list = ["id", "size", "x", "y"]
        for idx in my_list:
            dic[idx] = getattr(self, idx)
        return (dic)
