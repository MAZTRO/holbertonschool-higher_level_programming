#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    oun_dir = a_dictionary.copy()
    for key, value in oun_dir.items():
        oun_dir[key] = value * 2
    return oun_dir
