#!/usr/bin/python3

"""function that prints the list of attribut and methode"""


def lookup(obj):
    """function that prints the list of attribut and methode"""

    list = dir(obj)
    return list