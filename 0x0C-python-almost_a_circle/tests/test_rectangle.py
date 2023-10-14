#!/usr/bin/python3
"""
Unittest for Base Class
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 5, x, y, id=None)

    def test_validation(self):
        self.assertEqual(self.rectangle.get_width(), 10)
        self.assertEqual(self.rectangle.get_height(), 5)
        self.assertEqual(self.rectangle.get_x(), 0)
        self.assertEqual(self.rectangle.get_y(), 0)

    def two_arg(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id + 1, r2.id)

    def two_arg(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertnotEqual(r1.id, r2.id)

    
     def three_arg(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        self.assertEqual(r1.id + 1, r2.id)

    def three_arg(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        self.assertnotEqual(r1.id, r2.id)

    def four_arg(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 4, 5, 6)
        self.assertEqual(r1.id + 1, r2.id)

    def one_arg(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 4, 5, 6)
        self.assertnotEqual(r1.id, r2.id)
