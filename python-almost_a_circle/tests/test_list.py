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
    def test_rectangle_display(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Réinitialisez le flux de sortie standard
        mock_stdout = StringIO()

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()