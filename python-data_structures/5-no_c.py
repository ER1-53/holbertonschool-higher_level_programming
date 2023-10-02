#!/usr/bin/python3
def no_c(my_string):
    chars = 'cC'
    new_string = my_string.translate(str.maketrans('', '', chars))
    return new_string
