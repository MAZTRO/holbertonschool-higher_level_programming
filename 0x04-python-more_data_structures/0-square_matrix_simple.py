#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        oun_matrix = matrix.copy()

        for val in range(len(matrix)):
            oun_matrix[val] = list(map(lambda x: x ** 2, matrix[val]))
        return oun_matrix
