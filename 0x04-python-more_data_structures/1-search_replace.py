#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list):
        oun_list = my_list.copy()
        for value in range(len(my_list)):
            if oun_list[value] == search:
                oun_list[value] = replace
        return oun_list
