#!/usr/bin/python3
"""Base of the project"""


class Base:
    """ base fonction"""
    __nb_objects = 0

    def __init__(self, id=None):
        
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
