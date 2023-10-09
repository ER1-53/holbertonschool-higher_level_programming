#!/usr/bin/python3
"""
It's class Square for creat a square.
"""


class Square:
    """
    It's class Square for creat a square.
    """

    def __init__(self, size=0):

        """
        Initializes a new Square object with a given size.
        :param size: The side length of the square.
        :raises ValueError: If size is less than 0.
        :raises TypeError: If size is not an integer.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
