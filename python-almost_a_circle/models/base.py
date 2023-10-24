#!/usr/bin/python3
"""Base of the project"""
import json


class Base:
    """ base fonction"""
    __nb_objects = 0
    display_n = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        filename = cls.__name__ + ".json"
        list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(list_objs, file)
