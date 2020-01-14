#!/usr/bin/python3
"""function that multiplies 2 matrices.

    Returns: the new matrix
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices
        Args:
            m_a (list): Matrix (list of lists) 1
            m_b (list): Matrix (list of lists) 2
        Returns:
            the new Matrix (list of lists).
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for list_a in m_a:
        if type(list_a) is not list:
            raise TypeError("m_a must be a list of lists")

    for list_b in m_b:
        if type(list_b) is not list:
            raise TypeError("m_b must be a list of lists")

    for list_int in m_a:
        for value in list_int:
            if type(value) is not int and type(value) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for list_int in m_b:
        for value in list_int:
            if type(value) is not int and type(value) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if not m_a:
        raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_b can't be empty")

    for list_a in m_a:
        if len(list_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for list_b in m_b:
        if len(list_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    else:
        list_in = []
        new_list = []
        for x in range(len(m_b[0])):
            list_in.append(list(map(lambda i: i[x], m_b)))
        for y in m_a:
            tmp = []
            for z in list_in:
                tmp.append(sum(list(map(lambda j: y[j] * z[j],
                                        range(len(m_a[0]))))))
            new_list.append(tmp)

        return (new_list)
