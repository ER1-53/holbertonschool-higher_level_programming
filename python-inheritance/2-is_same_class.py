#!/usr/bin/python3

"""A function that checks if an object is
an instance of a specific class."""


def is_same_class(obj, a_class):

    """
    Check if the provided object is an instance
    of the specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if the object is an instance of
        the specified class, False otherwise.
    """

    return type(obj) is a_class
