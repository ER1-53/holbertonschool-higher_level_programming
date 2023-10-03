#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[0])):
            print("{:d}".format(matrix[row][element]), end="")
            if element < len(matrix[0]) - 1:
                print(" ",end="")
        print()
