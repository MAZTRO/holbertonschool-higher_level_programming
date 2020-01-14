#!/usr/bin/python3
"""function that divide a matrix by a integer.

    Returns: New matrix with the result
"""


def matrix_divided(matrix, div):
    """Function to divide:
        Args:
            Matrix (list): The lists to divide by div
            div (int): the divisor
        Returns:
            New matrix with the result
    """

    if (type(matrix) is not list or len(matrix) == 0):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if ((type(div) is not int) and (type(div) is not float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    res = []
    for length in matrix:
        if type(length) is not list or len(length) == 0:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if len(length) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for test_val in length:
            if (type(test_val) is not int) and (type(test_val) is not float):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            else:
                res.append(round(test_val / div, 2))
        new_list.append(res)
        res = []
    return (new_list)
