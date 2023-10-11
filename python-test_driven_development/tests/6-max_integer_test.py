#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""


import unittest


class test_unit(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    def test_max_int(self):
        numbers = [1, 2, 3, 4]
        max_value = max(numbers)
        self.assertEqual(max_value, 4)

    def test_max_with_neg(self):
        numbers = [-1, -2, -3, -4]
        max_value = max(numbers)
        self.assertEqual(max_value, -1)

    def test_max_int_empty_list(self):
        numbers = []
        max_value = None
        self.assertEqual(max_value, None)

    def test_str_fail(self):
        numbers = ["poupy", 4]
        with self.assertRaises(TypeError):
            max_value = max(numbers)


if __name__ == '__main__':
    unittest.main()
    