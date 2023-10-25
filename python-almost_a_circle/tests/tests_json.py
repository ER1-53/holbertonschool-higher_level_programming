#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_JSON(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_to_json_string(self):
        b = Base(1)
        expected_result = '[{"id": 1}]'
        self.assertEqual(Base.to_json_string([{'id': b.id}]), expected_result)
    
    def test_to_json_string_rect(self):
        r = Rectangle(10, 7, 2, 8)
        objects = [r.to_dictionary()]
        json_string = Base.to_json_string(objects)
        expected_result = '[{"y": 8, "width": 10, "x": 2, "id": 7, "height": 7}]'
        self.assertEqual(json_string, expected_result)

if __name__ == '__main__':
    unittest.main()