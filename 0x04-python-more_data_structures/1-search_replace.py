#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list):
        N = my_list.copy()
        N = list(map(lambda A: A if A != search else replace, N))
        return oun_list
