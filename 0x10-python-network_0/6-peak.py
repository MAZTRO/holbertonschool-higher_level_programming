#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    ls = list_of_integers
    peak = None

    if (list_of_integers):
        for idx in range(1, len(ls) - 1):
            if (ls[idx] >= ls[idx - 1] and ls[idx] >= ls[idx + 1]):
                if 
                peak = ls[idx]
    return (peak)
