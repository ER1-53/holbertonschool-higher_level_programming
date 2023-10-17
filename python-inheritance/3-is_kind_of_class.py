#!/usr/bin/python3

"""A function that checks if an object is an instance or a subclass of a specific class."""


def is_kind_of_class(obj, a_class):
    
    """
    Check if the provided object is an instance of the specified class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class or a subclass of it, False otherwise.
    """

    if not isinstance(obj, a_class) and not issubclass(type(obj), a_class):
        return False
    return True
