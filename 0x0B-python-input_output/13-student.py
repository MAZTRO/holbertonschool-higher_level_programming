#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list):
            new_dir = {}
            for keys in attrs:
                if type(keys) == str:
                    try:
                        new_dir[keys] = getattr(self, keys)
                    except AttributeError:
                        pass
            return new_dir
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        if (type(json) == dict):
            for key, value in json.items():
                setattr(self, key, value)
