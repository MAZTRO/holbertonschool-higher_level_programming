#!/usr/bin/python3
"""
    function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """ Prototype: def lookup(obj) """

    return (list(dir(obj)))
