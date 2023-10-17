#!/usr/bin/python3

"""A custom list class that can print itself sorted."""


class MyList(list):

    """that prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        if not all(isinstance(x, int) for x in self):
            raise TypeError("Not all elements in the list are integers")
        sorted_list = sorted(self)
        print(sorted_list)
