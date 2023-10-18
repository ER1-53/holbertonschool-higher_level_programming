#!/usr/bin/python3
""" function for write file"""


def write_file(filename="", text=""):
    """ function for write file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)