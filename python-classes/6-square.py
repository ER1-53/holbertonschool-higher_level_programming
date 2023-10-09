#!/usr/bin/python3
"""
It's class Square for creat a square.
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object with a given size and position.
        :param size: The side length of the square.
        :param position: A tuple representing the position of the square.
        :raises ValueError: If size is less than 0.
        :raises TypeError: If size is not an integer or position is not
        a tuple of 2 integers.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates and returns the area of the square.
        :return: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square at the specified position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
