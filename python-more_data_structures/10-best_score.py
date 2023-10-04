#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dict = sorted(a_dictionary.items())
    best_key, value = sorted_dict[0]
    return best_key
