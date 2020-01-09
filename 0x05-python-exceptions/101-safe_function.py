#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = 0
        res = fct(*args)
        return (res)
    except (TypeError, ValueError, ZeroDivisionError, IndexError) as stderror:
        sys.stderr.write("Exception: {}\n".format(stderror))
        return None
