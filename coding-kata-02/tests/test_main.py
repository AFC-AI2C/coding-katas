from main import *
import unittest

class TestMain(unittest.TestCase):
    def test_function_one(self):
        self.assertEqual(function_one(2, 3), 5)
        self.assertEqual(function_one(-1, 1), 0)
        self.assertEqual(function_one(0, 0), 0)

    def test_function_two(self):
        self.assertEqual(function_two(2, 3), 5)
        self.assertEqual(function_two(-1, 1), 0)
        self.assertEqual(function_two(0, 0), 0)

    def test_function_three(self):
        self.assertEqual(function_three(2, 3), 5)
        self.assertEqual(function_three(-1, 1), 0)
        self.assertEqual(function_three(0, 0), 0)
        with self.assertRaises(TypeError):
            function_three(2, "3")
        with self.assertRaises(TypeError):
            function_three("2", 3)