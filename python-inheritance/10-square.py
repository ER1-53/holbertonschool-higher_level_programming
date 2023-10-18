#!/usr/bin/python3
"""Base geometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square from rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
