#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        dic = []
        if len(list_objs) != 0:
            for obj in list_objs:
                name = obj.__class__.__name__
                dic.append(obj.to_dictionary())
                name += ".json"
            with open(name, "w") as file:
                file.write(cls.to_json_string(dic))
        else:
            name = cls.__name__
            name += ".json"
            with open(name, "w") as file:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        if json_string is not None or len(json_string) != 0:
            return (json.loads(json_string))
        else:
            return ([])

    @classmethod
    def create(cls, **dictionary):
        test = cls(20, 45, 63, 24)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        name = cls.__name__
        name += ".json"
        with open(name, "r") as my_file:
            inst = []
            ins_dic = cls.from_json_string(my_file.read())
            for dic in ins_dic:
                inst.append(cls.create(**dic))
        return inst
