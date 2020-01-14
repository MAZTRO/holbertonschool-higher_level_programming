#!/usr/bin/python3
"""
    Class that contain some test with UNITEST module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_Max(self):
        """ test the max function works correctly """
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)

    def test_Max_empty(self):
        """ test the max function works correctly """
        self.assertEqual(max_integer([]), None)

    def test_Max_neg(self):
        """ test the max function works correctly """
        self.assertEqual(max_integer([-10, -8, -20, -5000000]), -8)

    def test_Max_Err(self):
        """ test the max function works correctly """
        with self.assertRaises(TypeError):
            lis = [1, 2, 3, "Holberton"]
            max_integer(lis)

    def test_Max_zero(self):
        """ test the max function works correctly """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_empty(self):
        """ test the max function works correctly """
        self.assertIsNone(max_integer([]))

    def test_max_int(self):
        """ test the max function works correctly """
        self.assertEqual(max_integer([1, 5, 444444444]), 444444444)

    def test_float(self):
        """ test the max function works correctly """
        self.assertNotEqual(max_integer([4.2, 3, 5]), 4.2)

    def test_error(self):
        """ test the max function works correctly """
        with self.assertRaises(TypeError):
            self.assertRaises(max_integer(89))

    def test_is_not_max(self):
        """ test the max function works correctly """
        self.assertIsNot(max_integer([1, 4, 5]), 4)
