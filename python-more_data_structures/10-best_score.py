#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda x: x[1])
    best_key, best_value = sorted_dict[-1]
    return best_key
