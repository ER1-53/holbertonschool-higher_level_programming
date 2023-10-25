#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test(unittest.TestCase):    
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(100)
        self.assertEqual(b.id, 100)
        b = Base(-5)
        self.assertEqual(b.id, -5)
        b = Base("holbies")
        self.assertEqual(b.id, "holbies")
        b = Base("H")
        self.assertEqual(b.id, "H")
        b = Base(8.5)
        self.assertEqual(b.id, 8.5)
    
    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        with self.assertRaises(ValueError) as context:
            Rectangle(-20, 7, 2, 8)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 7, 2, 8)    
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 0, 2, 8)
        self.assertEqual(str(context.exception), "height must be > 0")
        with self.assertRaises(ValueError) as context:
            Rectangle(10, -7, 2, 8)
        self.assertEqual(str(context.exception), "height must be > 0")
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, -5, 8)
        self.assertEqual(str(context.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 7, 0, -8)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_init(self):
        s = Square(4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 4)
        s = Square(4)
        self.assertEqual(s.size, 4)
        s.size = 5
        self.assertEqual(s.size, 5)
        s = Square(4)
        s.update(6, size=7, x=1, y=2)
        self.assertEqual(s.id, 6)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        with self.assertRaises(ValueError) as context:
            Square(10, -7)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_to_json_string(self):
        b = Base(1)
        expected_result = '[{"id": 1}]'
        self.assertEqual(Base.to_json_string([{'id': b.id}]), expected_result)
        r = Rectangle(10, 7, 2, 8)
        objects = [r.to_dictionary()]
        json_string = Base.to_json_string(objects)
        expected_result = '[{"y": 8, "width": 10, "x": 2, "id": 5, "height": 7}]'
        self.assertEqual(json_string, expected_result)

if __name__ == '__main__':
    unittest.main()