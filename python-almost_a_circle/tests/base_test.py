#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_init_with_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_init_with_neg_custom_id(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_init_with_string_custom_id(self):
        b = Base("holbies")
        self.assertEqual(b.id, "holbies")

    def test_init_with_char_custom_id(self):
        b = Base("H")
        self.assertEqual(b.id, "H")

    def test_init_with_float_custom_id(self):
        b = Base(8.5)
        self.assertEqual(b.id, 8.5)

if __name__ == '__main__':
    unittest.main()