#!/usr/bin/python3

"""Base geometry class"""


class BaseGeometry:
    """A function that checks if an object is an instance of
the specified class or a subclass of it."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
