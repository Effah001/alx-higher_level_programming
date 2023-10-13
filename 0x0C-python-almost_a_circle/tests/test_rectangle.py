#!/usr/bin/python3
"""
Unittest for Base Class
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(width=10, height=5, x=0, y=0, id=None)

    def test_validation(self):
        self.assertEqual(self.rectangle.get_width(), 10)
        self.assertEqual(self.rectangle.get_height(), 5)
        self.assertEqual(self.rectangle.get_x(), 0)
        self.assertEqual(self.rectangle.get_y(), 0)

    def test_invalidity(self):
        with self.assertRaises(ValueError):
            Rectangle(width=-1, height=5, x=0, y=0)
        with self.assertRaises(ValueError):
            Rectangle(width=10, height=-5, x=0, y=0)
        with self.assertRaises(ValueError):
            Rectangle(width=10, height=5, x=-1, y=0)
