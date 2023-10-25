#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 4)

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
        b = Base('H')
        self.assertEqual(b.id, 'H')

    def test_init_with_float_custom_id(self):
        b = Base(8.5)
        self.assertEqual(b.id, 8.5)

    def test_create_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_id_generation(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj2.id, 3)

    def test_to_json_string(self):
        obj = Base()
        json_str = obj.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_save_to_file(self):
        obj = Base()
        obj.save_to_file([])

    def test_from_json_string(self):
        json_str = '[]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(obj_list, [])

    def test_create(self):
        with self.assertRaises(TypeError):
            dummy_dict = {'id': 1, 'name': 'test'}
            obj = Base.create(**dummy_dict)
            self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        pass

    def test_to_json_string_with_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json_string_with_none(self):
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

if __name__ == '__main__':
    unittest.main()