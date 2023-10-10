#!/usr/bin/python3
"""
Add two value, a and b
>>> matrix is an integer
>>> div is an integer
function open
"""

def matrix_divided(matrix, div):
    """
    divided

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
         raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    result = []
    for row in matrix:
        for element in row:
            result.append(round((element / div), 2))
    return result
    
    
    
