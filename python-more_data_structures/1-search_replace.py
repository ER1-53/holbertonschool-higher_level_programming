#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element == search:
            element = replace
        new_list.append(element)
    return new_list
