#!/usr/bin/python3

"""Base geometry class"""


class BaseGeometry:
    """A function that checks if an object is an instance of
the specified class or a subclass of it."""
    def area(self):
        raise Exception("area() is not implemented")
