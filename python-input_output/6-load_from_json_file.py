#!/usr/bin/python3
""" function for write file"""


import json


def load_from_json_file(filename):
    """ function for write file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
