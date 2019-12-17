#!/usr/bin/python3
def no_c(my_string):
    neg = ['c', 'C']
    my_string = ''.join(lett for lett in my_string if lett not in neg)
    return (my_string)
