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
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf8') as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if filename is None:
            return []
        return Base.from_json_string(Base.create(cls))

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []
