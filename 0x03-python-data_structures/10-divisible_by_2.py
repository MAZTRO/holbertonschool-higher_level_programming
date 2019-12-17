#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list):
        my_oun_list = my_list.copy()
        for div in my_oun_list:
            if (my_oun_list[div] % 2 == 0):
                my_oun_list[div] = True
            else:
                my_oun_list[div] = False
        return (my_oun_list)
