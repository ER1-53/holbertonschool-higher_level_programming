#!/usr/bin/python3
"""
Add two integers or
floats and return
the result as an
integer.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return the result as an integer.
    :param a: The first number (integer or float).
    :param b: The second number (integer or float).
    :return: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
