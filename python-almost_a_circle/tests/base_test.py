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

if __name__ == '__main__':
    unittest.main()