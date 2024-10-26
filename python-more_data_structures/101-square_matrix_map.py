#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    return list(map(list, map(lambda x: x * x, zip(*matrix))))

