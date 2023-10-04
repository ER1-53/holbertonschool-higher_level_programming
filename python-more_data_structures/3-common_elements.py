#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []
    for element in set_2:
        for element_t in set_1:
            if element == element_t:
                common_list.append(element)
    return common_list
