#!/usr/bin/python3
"""Base of the project"""


class Base:
    """ base fonction"""
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects
