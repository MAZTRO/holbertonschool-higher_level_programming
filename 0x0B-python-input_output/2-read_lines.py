#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as my_file:
        if nb_lines <= 0:
            my_file.seek(0)
            print(my_file.read())
        elif (nb_lines > len(my_file.readlines())):
            my_file.seek(0)
            print(my_file.read())
        else:
            my_file.seek(0)
            for line in range(nb_lines):
                line += 1
                print(my_file.readline() ,end='')
