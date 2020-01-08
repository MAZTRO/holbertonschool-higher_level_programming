#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a // b
        print("Inside result: {:d}".format(res))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return (None)
    finally:
        return (res)
