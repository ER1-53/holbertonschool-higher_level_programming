#!/usr/bin/python3

"""A function that checks if an object is an instance of
the specified class or a subclass of it."""


def inherits_from(obj, a_class):

    """
    Check if the provided object is an instance of the specified class
    or a subclass of it.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if the object is an instance of the specified class
        or a subclass of it, False otherwise.
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
