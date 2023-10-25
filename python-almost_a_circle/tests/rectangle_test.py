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
        self.assertEqual(r.id, 21)
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

    def test_create_instance(self):
        rect = Rectangle(2, 3)
        self.assertIsInstance(rect, Rectangle)

    def test_attributes_initialization(self):
        rect = Rectangle(2, 3, 1, 1, 7)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.id, 7)

    def test_width_property(self):
        rect = Rectangle(2, 3)
        rect.width = 4
        self.assertEqual(rect.width, 4)

    def test_height_property(self):
        rect = Rectangle(2, 3)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_x_property(self):
        rect = Rectangle(2, 3)
        rect.x = 2
        self.assertEqual(rect.x, 2)

    def test_y_property(self):
        rect = Rectangle(2, 3)
        rect.y = 2
        self.assertEqual(rect.y, 2)

    def test_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_display(self):
        rect = Rectangle(2, 3, 1, 2)
        expected_output = "\n" + " " * 1 + "##" + "\n" + " " * 1 + "##" + "\n" + " " * 1 + "##" + "\n"
        self.assertEqual(rect.display(), print(expected_output))

    def test_str_method(self):
        rect = Rectangle(2, 3, 1, 2, 7)
        expected_output = "[Rectangle] (7) 1/2 - 2/3"
        self.assertEqual(str(rect), expected_output)

    def test_update_method(self):
        rect = Rectangle(2, 3)
        rect.update(4, 5, 6, 7, 8)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_to_dictionary_method(self):
        rect = Rectangle(2, 3, 1, 2, 7)
        expected_dict = {'id': 7, 'width': 2, 'height': 3, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()