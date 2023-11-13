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
def test_set_y_to_maximum_value(self):
        """Vérifie que la position y de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5, 2, 3)
        square.y = 2**31 - 1
        self.assertEqual(square.y, 2**31 - 1)



if __name__ == '__main__':
    unittest.main()