#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
from io import StringIO
from unittest.mock import patch

class Test_General(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    def test_rectangle_exceptions(self):
        # Test de l'exception de type pour la hauteur
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, True)
        self.assertEqual(str(cm.exception), "height must be an integer")

        # Test de l'exception de valeur pour la largeur
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

        # Test de l'exception de type pour la position x
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2, True)
            r.x = {}
        self.assertEqual(str(cm.exception), "x must be an integer")

        # Test de l'exception de valeur pour la position y
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

if __name__ == '__main__':
    unittest.main()