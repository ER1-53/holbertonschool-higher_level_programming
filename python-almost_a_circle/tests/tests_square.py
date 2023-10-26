#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
import sys
import os
from io import StringIO
import unittest.mock
from models.square import Square
from models.rectangle import Rectangle

class Test_Square(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        s = Square(4)
        self.assertEqual(s.id, 150)
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

# ------------------------------------- #

    def setUp(self):
        """Initialisation d'une instance de Square avec une taille de 5."""
        self.s = Square(5)

    def tearDown(self):
        """Suppression de l'instance créée et du fichier Square.json
        s'il existe."""
        try:
            os.remove("Square.json")
        except Exception:
            pass
        del self.s

    def test_init_with_valid_values(self):
        """Vérifie que Square peut être initialisé avec des valeurs valides
        pour ses attributs."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_init_with_invalid_size(self):
        """Vérifie que Square génère une exception lorsqu'une taille
        invalide est utilisée pour l'initialisation."""
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_set_size_with_valid_value(self):
        """Vérifie que la taille de Square peut être modifiée avec une
        valeur valide."""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_set_size_with_invalid_value(self):
        """Vérifie que Square génère une exception lorsque la taille est
        définie avec une valeur invalide."""
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_str(self):
        """Vérifie que la méthode str renvoie une représentation sous forme
        de chaîne correcte de l'objet Square."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_with_args(self):
        """Vérifie que la méthode update met à jour les attributs de Square
        en utilisant des arguments positionnels."""
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        """Vérifie que la méthode update met à jour les attributs de Square
        en utilisant des arguments par mot-clé."""
        square = Square(5)
        square.update(id=1, size=10, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary(self):
        """Vérifie que la méthode to_dictionary renvoie un dictionnaire
        contenant les attributs de Square."""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_init_with_non_integer_size(self):
        """Vérifie que Square génère une exception lorsqu'une taille non
        entière est utilisée pour l'initialisation."""
        with self.assertRaises(TypeError):
            square = Square("invalid_size")

    def test_set_size_with_non_integer_value(self):
        """Vérifie que Square génère une exception lorsque la taille est
        définie avec une valeur non entière."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "invalid_size"

    def test_set_x_with_negative_value(self):
        """Vérifie que Square génère une exception lorsque la position x est
        définie avec une valeur négative."""
        square = Square(5, 2, 3)
        with self.assertRaises(ValueError):
            square.x = -1

    def test_set_y_with_negative_value(self):
        """Vérifie que Square génère une exception lorsque la position y est
        définie avec une valeur négative."""
        square = Square(5, 2, 3)
        with self.assertRaises(ValueError):
            square.y = -1

    def test_init_with_minimum_size(self):
        """Vérifie que Square peut être initialisé avec une taille minimale
        (1)."""
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_init_with_maximum_size(self):
        """Vérifie que Square peut être initialisé avec la taille maximale
        autorisée."""
        square = Square(2**31 - 1)
        self.assertEqual(square.size, 2**31 - 1)

    def test_set_size_to_maximum_value(self):
        """Vérifie que la taille de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5)
        square.size = 2**31 - 1
        self.assertEqual(square.size, 2**31 - 1)

    def test_init_with_minimum_x_and_y(self):
        """Vérifie que Square peut être initialisé avec des positions x et y
        minimales (0)."""
        square = Square(5, 0, 0)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_init_with_maximum_x_and_y(self):
        """Vérifie que Square peut être initialisé avec les positions x et y
        maximales autorisées."""
        square = Square(5, 2**31 - 1, 2**31 - 1)
        self.assertEqual(square.x, 2**31 - 1)
        self.assertEqual(square.y, 2**31 - 1)

    def test_set_x_to_maximum_value(self):
        """Vérifie que la position x de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5, 2, 3)
        square.x = 2**31 - 1
        self.assertEqual(square.x, 2**31 - 1)

    def test_set_y_to_maximum_value(self):
        """Vérifie que la position y de Square peut être définie à la valeur
        maximale autorisée."""
        square = Square(5, 2, 3)
        square.y = 2**31 - 1
        self.assertEqual(square.y, 2**31 - 1)


if __name__ == '__main__':
    unittest.main()
