#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] < my_list[j]:
                i = j
        return my_list[i]
