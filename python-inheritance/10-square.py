#!/usr/bin/python3
"""Base geometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A function init square"""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.size ** 2