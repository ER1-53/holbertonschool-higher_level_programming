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

        """
        Initializes a area of the Square.
        with calcul self.size * self.size
        """

        return self.__size ** 2

    @property
    def size(self):

        """
        With property is the solution for modif value
        Property is for getter
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        With .setter is the solution for modif value
        @instance.setter is for setter
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
