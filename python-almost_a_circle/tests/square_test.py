#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
import sys
from io import StringIO 
import unittest.mock
from models.square import Square

class Test_Square(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        s = Square(4)
        self.assertEqual(s.id, 43)
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
        with self.assertRaises(ValueError):
            Square(10, -7)

    def test_area(self):
        r = Square(2, 3)
        self.assertEqual(r.area(), 4)

    def test_area_revers(self):
        r = Square(3, 2)
        self.assertEqual(r.area(), 9)

    def test_area_bigger(self):
        r = Square(2, 10)
        self.assertEqual(r.area(), 4)

    def test_area_with_other_parameter(self):
        with self.assertRaises(TypeError):
            Square(8, 7, 0, 0, 12)

    def test_create_instance(self):
        square = Square(4)
        self.assertIsInstance(square, Square)

    def test_attributes_initialization(self):
        square = Square(4, 2, 3, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 7)

    def test_size_property(self):
        square = Square(4)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_update_method(self):
        square = Square(4)
        square.update(7, 5, 2, 3)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary_method(self):
        square = Square(4, 2, 3, 7)
        expected_dict = {'id': 7, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_display_with_default_x_y(self):
        square = Square(3)
        expected_output = "###\n" + "###\n" + "###\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_non_default_x_y(self):
        square = Square(3, 2, 1)
        expected_output = "\n" + "  ###\n" + "  ###\n" + "  ###\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_negative_x_y(self):
        with self.assertRaises(ValueError) as context:
            square = Square(3, -1, -2)
            square.display()

        expected_exception_message = "x must be >= 0"
        

    def test_display_with_size_1(self):
        square = Square(1, 2, 1)
        expected_output = "\n" + "  #\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_square_creation(self):
        square = Square(4, 2, 3, 7)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 7)

    def test_size_property(self):
        square = Square(2)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_update_method(self):
        square = Square(3, 1, 2, 4)
        square.update(7, 5, 6, 8)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)

    def test_to_dictionary_method(self):
        square = Square(3, 2, 1, 9)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 9, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()