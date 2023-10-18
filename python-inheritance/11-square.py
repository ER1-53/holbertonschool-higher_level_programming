#!/usr/bin/python3
"""Base geometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A function that checks if an object is an instance of
the specified class or a subclass of it."""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
    