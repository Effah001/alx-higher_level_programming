#!/usr/bin/python3
"""
Unittest for Base Class
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 5, 0, 0, id=None)

    def test_validation(self):
        self.assertEqual(self.rectangle.get_width(), 10)
        self.assertEqual(self.rectangle.get_height(), 5)
        self.assertEqual(self.rectangle.get_x(), 0)
        self.assertEqual(self.rectangle.get_y(), 0)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id + 1, r2.id)

    def test_two_args2(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertNotEqual(r1.id, r2.id)

     def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        self.assertEqual(r1.id + 1, r2.id)

    def test_three_args3(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        self.assertNotEqual(r1.id, r2.id)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 4, 5, 6)
        self.assertEqual(r1.id + 1, r2.id)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 4, 5, 6)
        self.assertNotEqual(r1.id, r2.id)

class TestRectangleArea(unittes.TestCase):
    def test_area1(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

    def test_area2(self):
        r1 = Rectangle(2, 3)
        self.assertNotEqual(r1.area(), 5)

    def test_area3(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.area(), r2.area())

    def test_area4(self):
        r1 = Rectangle(1, 3)
        r2 = Rectangle(2, 3)
        self.assertNotEqual(r1.area(), r2.area())



 
 

