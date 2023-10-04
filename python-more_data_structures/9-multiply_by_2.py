#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dico = {}
    for key, value in a_dictionary.items():
        new_dico[key] = value * 2
    return new_dico
