#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class test_unit(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    def test_max_end(self):
        numbers = [1, 2, 3, 4]
        max_value = max_integer(numbers)
        self.assertEqual(max_value, 4)

    def test_max_with_neg(self):
        numbers = [-1, -2, -3, -4]
        max_value = max_integer(numbers)
        self.assertEqual(max_value, -1)

    def test_max_int_empty_list(self):
        numbers = []
        max_value = max_integer(numbers)
        self.assertEqual(max_value, None)

    def test_str_fail(self):
        numbers = ["poupy", 4]
        with self.assertRaises(TypeError):
            max_value = max_integer(numbers)

    def test_max_allsame(self):
            numbers = [4, 4, 4, 4]
            max_value = max_integer(numbers)
            self.assertEqual(max_value, 4)

    def test_max_with_2int(self):
            numbers = [1, 21]
            max_value = max_integer(numbers)
            self.assertEqual(max_value, 21)

    def test_max_start(self):
            numbers = [51, 21, 15, 12]
            max_value = max_integer(numbers)
            self.assertEqual(max_value, 51)

    def test_max_mddl(self):
            numbers = [15, 21, 51, 12]
            max_value = max_integer(numbers)
            self.assertEqual(max_value, 51)

