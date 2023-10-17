#!/usr/bin/python3

"""function that prints the list of
attribut and methode"""


def is_kind_of_class(obj, a_class):
    """function that prints the list of
attribut and methode"""

    print(type(obj))
    if not type(obj) is a_class and not issubclass(type(obj), a_class):
        return False
    return True
