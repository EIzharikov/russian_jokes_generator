# pylint: skip-file
"""
Checks the Custom model generating joke function
"""

import unittest
from models.models_init import CustomRuGPT3Model


class CustomModelTest(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_model = CustomRuGPT3Model()

    def test_text_type_ideal(self):
        """
        Ideal joke generation scenario
        """
        expected = ''
        actual = self.custom_model.generate_joke('hello', 'eat', 40)
        self.assertEqual(type(expected), type(actual))

    def test_text_type_bad_input(self):
        """
        Invalid input text check
        """
        bad_inputs = [{}, (), None, 9, 9.34, True, [None]]
        expected = 0
        for bad_input in bad_inputs:
            actual = self.custom_model.generate_joke(bad_input, 'eat', 40)
            self.assertEqual(expected, actual)

    def test_max_len_bad_input(self):
        """
        Invalid input max_len check
        """
        bad_inputs = [10, 20, 150, 200]
        expected = 0
        for bad_input in bad_inputs:
            actual = self.custom_model.generate_joke('hello', 'eat', bad_input)
            self.assertEqual(expected, actual)

    def test_tag_bad_input(self):
        """
        Invalid input tag check
        """
        bad_inputs = [{}, (), None, 9, 9.34, True, [None]]
        expected = 0
        for bad_input in bad_inputs:
            actual = self.custom_model.generate_joke('hello', bad_input, 40)
            self.assertEqual(expected, actual)

    def test_nonexistent_tag(self):
        """
        Input non-existent tag check
        """
        expected = 0
        actual = self.custom_model.generate_joke('hello', 'education', 40)
        self.assertEqual(expected, actual)







