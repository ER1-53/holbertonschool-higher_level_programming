#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print("[", end="")
    for row in range(len(matrix)):
        print("[", end="")
        for column in range(len(matrix[0])):
            print("{:d}".format(matrix[column][row]**1), end="")
            if column < len(matrix[0]) - 1:
                print(", ", end="")
        if row < len(matrix) - 1:
            print("], ", end="")
        else:
            print("]", end="")
    print("]", end="")
    print()
