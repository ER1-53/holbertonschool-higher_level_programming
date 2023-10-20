#!/usr/bin/python3
""" function for write file"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  
        if triangle:
            prev_row = triangle[-1]  
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])  
            row.append(1) 
        triangle.append(row)

    return triangle 
