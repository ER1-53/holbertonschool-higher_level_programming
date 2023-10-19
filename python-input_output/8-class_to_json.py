#!/usr/bin/python3
""" function for write file"""
import json


def class_to_json(obj):
    return obj.__dict__
