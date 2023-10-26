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

        # Vérifiez les valeurs des attributs 'id'
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        # Vérifiez les valeurs des attributs 'id' pour chaque rectangle
        self.assertEqual(r1.id, 24)
        self.assertEqual(r2.id, 25)
        self.assertEqual(r3.id, 12)

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

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

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

    def test_rectangle_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_output)

        r2 = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] (26) 1/0 - 5/5"
        self.assertEqual(str(r2), expected_output)

    def test_rectangle_display_with_different_x_y_values(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "  ##\n  ##\n  ##\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Réinitialisez le flux de sortie standard
        mock_stdout = StringIO()

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (29) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/10 - 10/10")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 10/10")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 10/10")

    def test_rectangle_update_with_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (30) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (30) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (30) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_square_creation(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (33) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (34) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        expected_output = "  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (35) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        expected_output = " ###\n ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s3.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_square_size_property(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (36) 0/0 - 5")
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(str(s1), "[Square] (36) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as context:
            s1.size = "9"

        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

    def test_square_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (39) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_rectangle_to_dictionary_and_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(r1), "[Rectangle] (27) 1/9 - 10/2")
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 27, 'height': 2, 'width': 10})
        self.assertIsInstance(r1_dictionary, dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (28) 0/0 - 1/1")

        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (27) 1/9 - 10/2")
        self.assertFalse(r1 == r2)

    def test_square_to_dictionary_and_update(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1), "[Square] (37) 2/1 - 10")
        self.assertEqual(s1_dictionary, {'id': 37, 'x': 2, 'size': 10, 'y': 1})
        self.assertIsInstance(s1_dictionary, dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (38) 1/0 - 1")

        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (37) 2/1 - 10")
        self.assertFalse(s1 == s2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        
        expected_json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        
        self.assertEqual(json_string, expected_json_string)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            data = json.load(file)

        expected_data = [
            {"y": 8, "x": 2, "id": 31, "width": 10, "height": 7},
            {"y": 0, "x": 0, "id": 32, "width": 2, "height": 4}
        ]

        self.assertEqual(data, expected_data)

    def test_to_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)

        expected_json_output = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'

        self.assertEqual(json_list_input, expected_json_output)

    def test_from_json_string(self):
        json_list_input = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        list_output = Rectangle.from_json_string(json_list_input)

        expected_list_output = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        self.assertEqual(list_output, expected_list_output)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)  # Vérifie si l'objet est une instance de Rectangle
        self.assertEqual(r1.id, r2.id)  # Vérifie si les IDs sont identiques
        self.assertEqual(r1.width, r2.width)  # Vérifie si les largeurs sont identiques
        self.assertEqual(r1.height, r2.height)  # Vérifie si les hauteurs sont identiques
        self.assertEqual(r1.x, r2.x)  # Vérifie si les positions x sont identiques
        self.assertEqual(r1.y, r2.y)  # Vérifie si les positions y sont identiques

    def test_load_and_save_for_rectangles(self):
        # Create some rectangles
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        # Save rectangles to a file
        Rectangle.save_to_file(list_rectangles_input)

        # Load rectangles from the file
        list_rectangles_output = Rectangle.load_from_file()

        # Check if loaded data is identical to input data
        for rect_in, rect_out in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(rect_in.id, rect_out.id)
            self.assertEqual(rect_in.width, rect_out.width)
            self.assertEqual(rect_in.height, rect_out.height)
            self.assertEqual(rect_in.x, rect_out.x)
            self.assertEqual(rect_in.y, rect_out.y)

    def test_load_and_save_for_squares(self):
        # Create some squares
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        # Save squares to a file
        Square.save_to_file(list_squares_input)

        # Load squares from the file
        list_squares_output = Square.load_from_file()

        # Check if loaded data is identical to input data
        for square_in, square_out in zip(list_squares_input, list_squares_output):
            self.assertEqual(square_in.id, square_out.id)
            self.assertEqual(square_in.size, square_out.size)
            self.assertEqual(square_in.x, square_out.x)
            self.assertEqual(square_in.y, square_out.y)

if __name__ == '__main__':
    unittest.main()