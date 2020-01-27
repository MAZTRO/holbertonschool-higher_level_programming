#!/usr/bin/python3
""" Base File """


import json
import turtle


class Base:
    """ BASE """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To JSON """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON save """
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
        """ From JSON """
        if json_string is not None or len(json_string) != 0:
            return (json.loads(json_string))
        else:
            return ([])

    @classmethod
    def create(cls, **dictionary):
        """ Create """
        test = cls(20, 45, 63, 24)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """ Load """
        name = cls.__name__
        name += ".json"
        try:
            with open(name, "r") as my_file:
                inst = []
                ins_dic = cls.from_json_string(my_file.read())
                for dic in ins_dic:
                    inst.append(cls.create(**dic))
            return inst
        except:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ SAVE CSV """
        dic = []
        if len(list_objs) != 0:
            for obj in list_objs:
                name = obj.__class__.__name__
                dic.append(obj.to_dictionary())
                name += ".csv"
            with open(name, "w") as file:
                file.write(cls.to_json_string(dic))
        else:
            name = cls.__name__
            name += ".csv"
            with open(name, "w") as file:
                file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """ LOAD CSV """
        name = cls.__name__
        name += ".csv"
        with open(name, "r") as my_file:
            inst = []
            ins_dic = cls.from_json_string(my_file.read())
            for dic in ins_dic:
                inst.append(cls.create(**dic))
        return inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ DRAW """
        turtle.title("Holberton Grafics   --    by Jonatan Mazo")
        turtle.colormode(255)
        turtle.setup(width=1280, height=720, startx=0, starty=0)
        turtle.bgcolor(255, 255, 255)
        turtle.pensize(3)
        list_dict = []
        for figure in list_rectangles:
            list_dict.append(figure.to_dictionary())
        count = 0
        colors = ["Red", "FireBrick", "Dark Red"]

        turtle.color("Red")
        turtle.write("Rectangle task", False, "center", ("", 60, ""))
        turtle.penup()
        turtle.setposition(0, -30)
        turtle.pendown()
        turtle.write("by: jonatan Mazo", False, "center", ("", 20, ""))
        turtle.penup()
        turtle.setposition(-320, -180)
        turtle.pendown()
        turtle.pencolor("dark red")
        turtle.delay(100)
        turtle.forward(640)

        turtle.clear()
        for attr in list_dict:
            turtle.delay(0)
            turtle.penup()
            turtle.setposition(attr["x"], attr["y"])
            turtle.pendown()
            turtle.pencolor(colors[count])
            turtle.delay(10)
            print(attr)
            for edge in range(2):
                turtle.forward(attr["width"])
                turtle.left(90)
                turtle.forward(attr["height"])
                turtle.left(90)
            count += 1

        turtle.delay(0)
        turtle.penup()
        turtle.setposition(-320, -180)
        turtle.pendown()
        turtle.pencolor("dark red")
        turtle.delay(100)
        turtle.forward(640)
        turtle.clear()

        turtle.delay(0)
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()
        turtle.color("Red")
        turtle.write("Square task", False, "center", ("", 60, ""))
        turtle.penup()
        turtle.setposition(0, -30)
        turtle.pendown()
        turtle.write("by: jonatan Mazo", False, "center", ("", 20, ""))
        turtle.penup()
        turtle.setposition(-320, -180)
        turtle.pendown()
        turtle.pencolor("dark red")
        turtle.delay(100)
        turtle.forward(640)
        turtle.clear()

        list_dict = []
        for figure in list_squares:
            list_dict.append(figure.to_dictionary())

        count = 0
        colors = ["Red", "FireBrick", "Dark Red"]

        for attr in list_dict:
            turtle.delay(0)
            turtle.penup()
            turtle.setposition(attr["x"], attr["y"])
            turtle.pendown()
            turtle.pencolor(colors[count])
            turtle.delay(10)
            print(attr)
            for edge in range(4):
                turtle.forward(attr["size"])
                turtle.left(90)
            count += 1

        turtle.delay(0)
        turtle.penup()
        turtle.setposition(-320, -180)
        turtle.pendown()
        turtle.pencolor("dark red")
        turtle.delay(100)
        turtle.forward(640)
        turtle.clear()

        turtle.clear()
        turtle.delay(0)
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()
        turtle.color("Red")
        turtle.write("Thanks for watch", False, "center", ("", 60, ""))
        turtle.penup()
        turtle.setposition(0, -30)
        turtle.pendown()
        turtle.write("Holberton", False, "center", ("", 20, ""))
        turtle.penup()
        turtle.setposition(-320, -180)
        turtle.pendown()
        turtle.pencolor("dark red")
        turtle.delay(20)
        turtle.forward(640)
        turtle.clear()

        turtle.delay(0)
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()
        turtle.clear()
        red = 0
        for sp in range(300):
            if red < 252:
                red += 2
            else:
                red = 253
            turtle.pencolor(red, 0, 0)
            turtle.pensize(sp / 90)

            for tri in range(5):
                turtle.forward(4 * (sp / 2))  # Size of pligon
                turtle.left(45)  # degrees to make a polygon
            turtle.left(sp / 100)

        turtle.penup()
        turtle.setposition(0, 300)
        turtle.pendown()
        turn = turtle.heading()
        turtle.left(360 - turn)
        turtle.pencolor("White")
        turtle.pensize(20)
        turtle.backward(100)
        turtle.forward(200)
        turtle.penup()
        turtle.setposition(0, 290)
        turtle.pendown()
        turtle.color("Black")
        turtle.write("Click to close", False, "center", ("", 10, ""))
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()

        print("\nprocess successfully completed")
        print("\n----------------------------\n")
        print("waiting for a click to close the turtle window")
        turtle.exitonclick()  # Use a click of mouse to exit
