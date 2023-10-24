#!/usr/bin/python3
"""Base of the project"""
import json


class Base:
    """ base fonction"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return JSON string representation"""
        if list_dictionaries is None:
            return []
        else:
            representation = json.dumps(list_dictionaries)
            return representation
