#!/usr/bin/python3
""" function for write file"""


import json


def save_to_json_file(my_obj, filename):
    """ function for write file"""
    with open(filename, 'a', encoding="utf-8") as file:
        json.dump(my_obj, file)
