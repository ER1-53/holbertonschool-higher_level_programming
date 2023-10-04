#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for value in my_list:
        new_list.append(number*value)
    return new_list
