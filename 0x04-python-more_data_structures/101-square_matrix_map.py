#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda Row: list(map(lambda Col: Col ** 2, Row)), matrix))
