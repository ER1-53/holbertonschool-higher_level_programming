#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
import sys
from io import StringIO 
from models.rectangle import Rectangle
from unittest.mock import patch

class Test_Rectangle(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 24)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_Rectangle_width_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-20, 7, 2, 8)

    def test_Rectangle_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 7, 2, 8)

    def test_Rectangle_height_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 2, 8)

    def test_Rectangle_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -7, 2, 8)

    def test_Rectangle_x_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 7, -5, 8)

    def test_Rectangle_y_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 7, 0, -8)

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_revers(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_bigger(self):
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    def test_area_with_other_parameter(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_with_other_parameter(self):
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_create_instance(self):
        rect = Rectangle(2, 3)
        self.assertIsInstance(rect, Rectangle)

    def test_attributes_initialization(self):
        rect = Rectangle(2, 3, 1, 1, 7)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.id, 7)

    def test_width_property(self):
        rect = Rectangle(2, 3)
        rect.width = 4
        self.assertEqual(rect.width, 4)

    def test_height_property(self):
        rect = Rectangle(2, 3)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_x_property(self):
        rect = Rectangle(2, 3)
        rect.x = 2
        self.assertEqual(rect.x, 2)

    def test_y_property(self):
        rect = Rectangle(2, 3)
        rect.y = 2
        self.assertEqual(rect.y, 2)

    def test_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_display(self):
        rect = Rectangle(2, 3, 1, 2)
        expected_output = "\n" + " " * 1 + "##" + "\n" + " " * 1 + "##" + "\n" + " " * 1 + "##" + "\n"
        self.assertEqual(rect.display(), print(expected_output))

    def test_str_method(self):
        rect = Rectangle(2, 3, 1, 2, 7)
        expected_output = "[Rectangle] (7) 1/2 - 2/3"
        self.assertEqual(str(rect), expected_output)

    def test_update_method(self):
        rect = Rectangle(2, 3)
        rect.update(4, 5, 6, 7, 8)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_to_dictionary_method(self):
        rect = Rectangle(2, 3, 1, 2, 7)
        expected_dict = {'id': 7, 'width': 2, 'height': 3, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_display_with_different_x_y_values(self):
        rect = Rectangle(3, 2, 2, 1)
        
        expected_output = "\n" + "  ###\n" + "  ###\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        rect = Rectangle(3, 2, 0, 0)
        
        expected_output = "###\n" + "###\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        with self.assertRaises(ValueError) as context:
            rect = Rectangle(3, 2, -1, -2)
        
        expected_exception_message = "x must be >= 0"
        self.assertEqual(str(context.exception), expected_exception_message)
    
    def test_str_method_with_square(self):
        square = Rectangle(4, 4, 0, 0, 1)
        expected_output = "[Rectangle] (1) 0/0 - 4"
        self.assertEqual(str(square), expected_output)

    def test_str_method_with_non_square(self):
        rect = Rectangle(3, 5, 1, 2, 2)
        expected_output = "[Rectangle] (2) 1/2 - 3/5"
        self.assertEqual(str(rect), expected_output)

    def test_str_method_with_triangle(self):
        triangle = Rectangle(3, 5, 0, 0, 3)
        expected_output = "[Rectangle] (3) 0/0 - 3/5"
        self.assertEqual(str(triangle), expected_output)

    def test_update_with_one_argument(self):
        rect = Rectangle(2, 3)
        rect.update(7)
        self.assertEqual(rect.id, 7)

    def test_update_with_two_arguments(self):
        rect = Rectangle(2, 3)
        rect.update(7, 4)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 4)

    def test_update_with_keyword_arguments(self):
        rect = Rectangle(2, 3)
        rect.update(id=7, width=4, height=5, x=1, y=2)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_update_with_mixed_arguments_and_keywords(self):
        rect = Rectangle(2, 3)
        rect.update(7, width=4, x=1)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.x, 0)

    def test_update_with_empty_argument_list(self):
        rect = Rectangle(2, 3, 1, 2, 7)
        rect.update()
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_to_dictionary_default_values(self):
        # Create a Rectangle with default values
        rect = Rectangle(1, 1)
        expected_dict = {'id': 25, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_non_default_values(self):
        # Create a Rectangle with non-default values
        rect = Rectangle(3, 2, 2, 1, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_after_property_change(self):
        # Create a Rectangle and change its properties
        rect = Rectangle(3, 2, 2, 1, 7)
        rect.width = 5
        rect.height = 4
        expected_dict = {'id': 7, 'width': 5, 'height': 4, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_multiple_rectangles(self):
        # Create multiple rectangles and check their dictionaries
        rect1 = Rectangle(2, 1, 0, 0, 1)
        rect2 = Rectangle(3, 3, 1, 1, 2)
        rect3 = Rectangle(4, 4, 2, 2, 3)
        expected_dict1 = {'id': 1, 'width': 2, 'height': 1, 'x': 0, 'y': 0}
        expected_dict2 = {'id': 2, 'width': 3, 'height': 3, 'x': 1, 'y': 1}
        expected_dict3 = {'id': 3, 'width': 4, 'height': 4, 'x': 2, 'y': 2}
        self.assertEqual(rect1.to_dictionary(), expected_dict1)
        self.assertEqual(rect2.to_dictionary(), expected_dict2)
        self.assertEqual(rect3.to_dictionary(), expected_dict3)

if __name__ == '__main__':
    unittest.main()