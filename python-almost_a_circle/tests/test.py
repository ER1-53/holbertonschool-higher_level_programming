#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_base_initialization_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
    
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 5)

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


    """test rectangle"""

    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 14)
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
        with self.assertRaises(ValueError) as context:
            Rectangle(10, -7, 2, 8)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_Rectangle_x_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, -5, 8)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_Rectangle_y_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, 0, -8)
        self.assertEqual(str(context.exception), "y must be >= 0")


    """test square"""
    def test_init(self):
        s = Square(4)
        self.assertEqual(s.id, 15)
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
        with self.assertRaises(ValueError) as context:
            Square(10, -7, 2, 8)
        self.assertEqual(str(context.exception), "x must be >= 0")


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
        expected_result = '[{"y": 8, "width": 10, "x": 2, "id": 6, "height": 7}]'
        self.assertEqual(json_string, expected_result)

if __name__ == '__main__':
    unittest.main()