#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_Max(self):
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)

    def test_Max_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_Max_neg(self):
        self.assertEqual(max_integer([-10, -8, -20, -5000000]), -8)

    def test_Max_Err(self):
        with self.assertRaises(TypeError):
            lis = [1, 2, 3, "Holberton"]
            max_integer(lis)

    def test_Max_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_int(self):
        self.assertEqual(max_integer([1, 5, 444444444]), 444444444)

    def test_float(self):
        self.assertNotEqual(max_integer([4.2, 3, 5]), 4.2)

    def test_error(self):
        with self.assertRaises(TypeError):
            self.assertRaises(max_integer(89))

    def test_is_not_max(self):
        self.assertIsNot(max_integer([1, 4, 5]), 4)
