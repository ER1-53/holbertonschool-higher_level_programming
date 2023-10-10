#!/usr/bin/python3
"""
Divide a matrix by a divisor and round the results to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by the given
    divisor and round to two decimal places.
    :param matrix: A matrix (list of lists) of integers/floats.
    :param div: The divisor (number).
    :return: A new matrix with the results of the division.
    """
    error_M = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_M)
    elif any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        row_in_result = []
        for element in row:
            row_in_result.append(round((element / div), 2))
        result.append(row_in_result)
    return result
