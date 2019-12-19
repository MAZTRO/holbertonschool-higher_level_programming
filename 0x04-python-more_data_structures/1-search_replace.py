#!/usr/bin/python3
def search_replace(my_list, search, replace):
    N = my_list.copy()
    N = list(map(lambda A: A if A != search else replace, N))
    return N
