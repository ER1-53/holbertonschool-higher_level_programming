#!/usr/bin/python3

"""
A function that prints a square of a given size.
"""


def print_square(size):
    """
    Print a square of a specified size using '#' characters.

    :param size: The size of the square (an integer).
    :return: None
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
