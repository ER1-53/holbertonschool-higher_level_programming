#!/usr/bin/python3
"""
It's class Square for creat a square.
"""


class Square:
    """
    Size is for define size of square.
    """

    def __init__(self, size=0):

        """
        Initializes a new Square object with a given size.
        :param size: The side length of the square.
        :raises ValueError: If size is less than 0.
        :raises TypeError: If size is not an integer.
        """

        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
