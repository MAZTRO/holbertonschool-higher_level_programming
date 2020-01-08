#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a // b
        print("Inside result: {:d}".format(res))
        return (res)
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return (None)
