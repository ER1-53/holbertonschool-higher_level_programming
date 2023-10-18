#!/usr/bin/python3
""" function for write file"""


import json


def to_json_string(my_obj):
    """ function for write file"""
    x = json.dumps(my_obj)
    return x
