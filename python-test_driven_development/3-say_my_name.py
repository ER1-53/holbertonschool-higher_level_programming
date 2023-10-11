#!/usr/bin/python3

"""
A function that says the full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name by combining first_name and last_name.

    :param first_name: The first name (a string).
    :param last_name: The last name (a string, optional,
    default is an empty string).
    :return: None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name and not last_name:
        return None
    print("My name is {} {}".format(first_name, last_name))
