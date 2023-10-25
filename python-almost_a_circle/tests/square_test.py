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
        self.assertEqual(s.id, 12)
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
            Square(10, -7)
        self.assertEqual(str(context.exception), "x must be >= 0")

if __name__ == '__main__':
    unittest.main()