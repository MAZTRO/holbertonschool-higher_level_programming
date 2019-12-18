#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_0, add_1 = 0, 0
    if (not tuple_a) and (not tuple_b):
        add_0 = 0
        add_1 = 0
        tuple_c = (add_0, add_1)
        return (tuple_c)
    if (not tuple_a):
        return (tuple_b)
    if (not tuple_b):
        return (tuple_a)
    if (len(tuple_a) >= 2 and len(tuple_b) >= 2):
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = tuple_a[1] + tuple_b[1]
        tuple_c = (add_0, add_1)
        return (tuple_c)
    if len(tuple_a) < 2 and len(tuple_b) < 2:
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = 0
        tuple_c = (add_0, add_1)
        return (tuple_c)
    if len(tuple_a) < 2:
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = tuple_b[1]
        tuple_c = (add_0, add_1)
        return (tuple_c)
    if len(tuple_b) < 2:
        add_0 = tuple_a[0] + tuple_b[0]
        add_1 = tuple_a[1]
        tuple_c = (add_0, add_1)
        return (tuple_c)
