#!/usr/bin/python3
"""
Unittest for Base Class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

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

class TestRectangleArea(unittest.TestCase):
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

class TestRectangleDisplay(unittest.TestCase):
    def test_display(self):
         r1 = Rectangle(3, 2)
         expected_output = "###\n###\n"
         
         with patch("sys.stdout", new=StringIO()) as new_output:
             r1.display()
             self.assertEqual(new_output.getvalue(), expected_output)

    def test_display_5x4(self):
        r2 = Rectangle(5, 4)
        expected_output = "#####\n#####\n#####\n#####\n"

        with patch("sys.stdout", newStringIO) as new_output:
            r2.display()
            self.assertEqual(new_output.getvalue(), expected_output)

    def test_display_1x1(self):
        r3 = Rectangle(5, 4)
        expected_output = "#\n"

        with patch("sys.stdout", new=StringIO) as new_output:
            r3.display()
            self.assertEqual(new_output.getvalue(), expected_output)

class TestStrMethod(unittest.TestCase):
    def test_str(self):
        rectangle = Rectangle(4, 2, 1, 2, 1)
        expected_output = "[Rectangle] (1) 1/2 - 4/2"
        self.assertEqual(str(rectangle), expected_output)

    def test_str2(self):
        rectangle = Rectangle(5, 3, 2, 3, 2)
        expected_output = "[Rectangle] (2) 2/3 - 5/3"
        self.assertEqual(str(rectangle), expected_output)

    def test_str(self):
        rectangle = Rectangle(4, 2, 1)
        expected_output = "[Rectangle] (1) 1/0 - 4/2"
        self.assertEqual(str(rectangle), expected_output)

class TestRectangleDisplayWithOffset(unittest.TestCase):
    def test_display_offset(self):
         r1 = Rectangle(3, 2, 1, 2)
         expected_output = "  ###\n ###\n"
         
         with patch("sys.stdout", new=StringIO()) as new_output:
             r1.display()
             self.assertEqual(new_output.getvalue(), expected_output)

    def test_display_5x4(self):
        r2 = Rectangle(5, 4, 1, 0)
        expected_output = "#####\n #####\n #####\n #####\n"

        with patch("sys.stdout", new=StringIO) as new_output:
            r2.display()
            self.assertEqual(new_output.getvalue(), expected_output)
