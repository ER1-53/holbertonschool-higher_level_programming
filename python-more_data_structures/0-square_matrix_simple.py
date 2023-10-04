#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        result.append(new_row)
    return result
