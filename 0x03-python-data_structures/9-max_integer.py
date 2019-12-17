#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        temp = my_list[0]
        for big in my_list:
            if (big >= temp):
                temp = big
        return (temp)
