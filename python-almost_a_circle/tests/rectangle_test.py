#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
import sys
from io import StringIO 
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_Rectangle_width_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-20, 7, 2, 8)

    def test_Rectangle_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 7, 2, 8)

    def test_Rectangle_height_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 2, 8)

    def test_Rectangle_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -7, 2, 8)

    def test_Rectangle_x_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 7, -5, 8)

    def test_Rectangle_y_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 7, 0, -8)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_revers(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_bigger(self):
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    def test_area_with_other_parameter(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_with_other_parameter(self):
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

if __name__ == '__main__':
    unittest.main()