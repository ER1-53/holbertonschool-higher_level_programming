#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_Rectangle_width_neg(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-20, 7, 2, 8)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_Rectangle_width_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 7, 2, 8)    
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_Rectangle_height_neg(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 0, 2, 8)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_Rectangle_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -7, 2, 8)

    def test_Rectangle_x_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, -5, 8)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_Rectangle_y_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, 0, -8)
        self.assertEqual(str(context.exception), "y must be >= 0")

if __name__ == '__main__':
    unittest.main()