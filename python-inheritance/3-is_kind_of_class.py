#!/usr/bin/python3

"""function that prints the list of
attribut and methode"""


def is_kind_of_class(obj, a_class):
    """function that prints the list of
attribut and methode"""

    if not isinstance(obj, a_class) and not issubclass(type(obj), a_class):
        return False
    return True
