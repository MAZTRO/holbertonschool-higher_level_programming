#!/usr/bin/python3
"""function that adds 2 integers.
    Returns an integer: the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def matrix_divided(matrix, div):
    """
        a and b must be first casted to integers if they are float
    """
    if ((type(div) is not int) and (type(div) is not float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) is not list):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    new_list = []
    res = []
    for length in matrix:
        if len(length) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if type(length) is not list:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        for test_val in length:
            if (type(test_val) is not int) and (type(test_val) is not float):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            else:
                res.append(round(test_val / div, 2))
        new_list.append(res)
        res = []
    return (new_list)
