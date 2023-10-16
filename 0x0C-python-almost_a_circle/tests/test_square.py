#!/usr/bin/python3
"""
Unittest for square class
"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square


class Testsquare(unittest.TestCase):
    def test_square(self):
        s1 = Square(5, 4, 3, 2)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 2)

    def test_square(self):
        s2 = Square(4, 3, 2, 1)
        self.assertEqual(s2.width, 4)
        self.assertEqual(s2.height, 4)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 1)

    def test_size(self):
        s3 = Square(2)
        self.assertEqual(s3.size, 2)
        s4 = Square(3)
        self.assertEqual(s4.size, 3)

    def test_update(self):
        s1 = Square(2, 3, 4, 5)
        s1.update(5, 4, 3, 2)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)


    def test_str(self):
        s5 = Square(2, 3, 3, 4)
        self.assertEqual(str(s5), "[Square] (4) 3/3 - 2")
