#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list):
        pos = 0
        for div in my_list:
            if (pos % 2 == 0):
                my_oun_list.insert(pos, True)
            else:
                my_oun_list.insert(pos, False)
            pos += 1
        return (my_oun_list)
