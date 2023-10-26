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
    def test_base(self):
        # Créez plusieurs instances de Base
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

if __name__ == '__main__':
    unittest.main()