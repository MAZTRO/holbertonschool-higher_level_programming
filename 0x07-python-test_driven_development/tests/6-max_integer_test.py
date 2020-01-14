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

    def test_Max_int(self):
        self.assertIsNot(max_integer([-4535943, 0]), 1)

    def test_Max_Err(self):
        with self.assertRaises(TypeError):
            lis = [1, 2, 3, "Holberton"]
            max_integer(lis)

    def test_Max_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
