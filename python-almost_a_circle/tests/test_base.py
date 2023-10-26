#!/usr/bin/python3
"""Module to test the condition of max integer in a list
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class Test_Base(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 6)

    def test_init_with_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_init_with_neg_custom_id(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_init_with_string_custom_id(self):
        b = Base("holbies")
        self.assertEqual(b.id, "holbies")

    def test_init_with_char_custom_id(self):
        b = Base('H')
        self.assertEqual(b.id, 'H')

    def test_init_with_float_custom_id(self):
        b = Base(8.5)
        self.assertEqual(b.id, 8.5)

    def test_create_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_id_generation(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 4)
        self.assertEqual(obj2.id, 5)

    def test_to_json_string(self):
        obj = Base()
        json_str = obj.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_save_to_file(self):
        obj = Base()
        obj.save_to_file([])

    def test_create(self):
        with self.assertRaises(TypeError):
            dummy_dict = {'id': 1, 'name': 'test'}
            obj = Base.create(**dummy_dict)
            self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        pass

# --------------------------------------------- #

    def test_creation_with_id(self):
        """Vérifie si un objet est créé avec l'ID spécifié."""
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_creation_without_id(self):
        """Vérifie que la classe Base attribue automatiquement des IDs
        incrémentiels aux objets créés."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj2.id, 3)

    def test_private_nb_objects_no_direct_access(self):
        """S'assure qu'il n'y a pas d'accès direct à l'attribut privé
        __nb_objects."""
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_to_json_string_with_data(self):
        """Vérifie que la méthode to_json_string convertit correctement des
        données en format JSON."""
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, json.dumps(data))

    def test_to_json_string_with_empty_data(self):
        """Vérifie que to_json_string gère correctement une liste vide."""
        data = []
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_none_data(self):
        """Vérifie que to_json_string gère correctement une valeur None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_with_empty_data(self):
        """Vérifie la sauvegarde de données JSON dans un fichier et leur
        lecture pour vérifier l'intégrité des données."""
        data = []
        filename = "Base.json"
        Base.save_to_file(data)
        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_save_to_file_with_none_data(self):
        """Vérifie la gestion de la valeur None lors de la sauvegarde dans
        un fichier."""
        filename = "Base.json"

        Base.save_to_file(None)

        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_from_json_string_with_data(self):
        """Vérifie que la méthode from_json_string peut convertir une chaîne
        JSON en une structure de données Python."""
        data = [{'key1': 'value1', 'key2': 'value2'}]
        json_str = json.dumps(data)
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, data)

    def test_from_json_string_with_empty_data(self):
        """Vérifie que from_json_string gère correctement une chaîne
        JSON vide."""
        json_str = "[]"
        loaded_data = Base.from_json_string(json_str)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_with_none_data(self):
        """Vérifie que from_json_string gère correctement la valeur None."""
        loaded_data = Base.from_json_string(None)
        self.assertEqual(loaded_data, [])

    def test_init_with_zero_id(self):
        """Vérifie que la classe Base accepte un ID de zéro."""
        base = Base(0)
        self.assertEqual(base.id, 7)

    def test_init_with_maximum_id(self):
        """Vérifie que la classe Base accepte un ID maximum autorisé."""
        base = Base(2**31 - 1)
        self.assertEqual(base.id, 2**31 - 1)

    def test_set_id_to_maximum_value(self):
        """Vérifie que la classe Base accepte de définir l'ID à la valeur
        maximale autorisée."""
        base = Base()
        base.id = 2**31 - 1
        self.assertEqual(base.id, 2**31 - 1)

if __name__ == '__main__':
    unittest.main()
