#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.square import Square

class Test_Square(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        s = Square(4)
        self.assertEqual(s.id, 31)
        self.assertEqual(s.size, 4)

    def test_size_property(self):
        s = Square(4)
        self.assertEqual(s.size, 4)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_update(self):
        s = Square(4)
        s.update(6, size=7, x=1, y=2)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_Square_size_zero(self):
        with self.assertRaises(ValueError):
            Square(10, -7)

    def test_area(self):
        r = Square(2, 3)
        self.assertEqual(r.area(), 4)

    def test_area_revers(self):
        r = Square(3, 2)
        self.assertEqual(r.area(), 9)

    def test_area_bigger(self):
        r = Square(2, 10)
        self.assertEqual(r.area(), 4)

    def test_area_with_other_parameter(self):
        with self.assertRaises(TypeError):
            Square(8, 7, 0, 0, 12)

    def test_create_instance(self):
        square = Square(4)
        self.assertIsInstance(square, Square)

    def test_attributes_initialization(self):
        square = Square(4, 2, 3, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 7)

    def test_size_property(self):
        square = Square(4)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_update_method(self):
        square = Square(4)
        square.update(7, 5, 2, 3)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary_method(self):
        square = Square(4, 2, 3, 7)
        expected_dict = {'id': 7, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()