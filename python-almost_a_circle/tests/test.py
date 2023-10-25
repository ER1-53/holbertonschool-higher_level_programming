#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
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

    def test_rectangle_initialization_id(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)
        r3 = Rectangle(2, 5)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        r4 = Rectangle(3,6,1)
        self.assertEqual(r4.id, 6)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 0)
        r5 = Rectangle(1 ,2, 3, 4, 20)
        self.assertEqual(r5.id, 20)
        self.assertEqual(r5.width, 1)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 4)

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, -5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, "-5")
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, [-5])
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, {-5})

    def test_square_initialization_id(self):
        with self.assertRaises(TypeError):
            s1 = Square()
        s1 = Square(3)
        self.assertEqual(s1.id, 12)


if name == 'main':
    unittest.main()