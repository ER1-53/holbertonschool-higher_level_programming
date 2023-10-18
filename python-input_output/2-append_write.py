#!/usr/bin/python3
""" function for write file"""


def append_write(filename="", text=""):
    """ function for write file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
