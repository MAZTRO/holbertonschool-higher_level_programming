#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
        return (res)
    except ZeroDivisionError:
        res = None
        return (None)
    finally:
        print("Inside result: {}".format(res))
