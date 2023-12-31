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

        with patch("sys.stdout", new=StringIO()) as new_output:
            r2.display()
            self.assertEqual(new_output.getvalue(), expected_output)

    def test_display_1x1(self):
        r3 = Rectangle(1, 1)
        expected_output = "#\n"

        with patch("sys.stdout", new=StringIO()) as new_output:
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

    def test_str3(self):
        rectangle = Rectangle(4, 2, 1, 1, 3)
        expected_output = "[Rectangle] (3) 1/1 - 4/2"
        self.assertEqual(str(rectangle), expected_output)

class TestRectangleDisplayWithOffset(unittest.TestCase):
    def test_display_offset(self):
         r1 = Rectangle(3, 2, 1, 2)
         expected_output = "\n\n ###\n ###\n"
         
         with patch("sys.stdout", new=StringIO()) as new_output:
             r1.display()
             self.assertEqual(new_output.getvalue(), expected_output)

    def test_display_5x4(self):
        r2 = Rectangle(5, 4, 1, 0)
        expected_output = " #####\n #####\n #####\n #####\n"

        with patch("sys.stdout", new=StringIO()) as new_output:
             r2.display()
             self.assertEqual(new_output.getvalue(), expected_output)

class TestUpdateValue(unittest.TestCase):
    def test_update_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_args2(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_args3(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50, 60)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_args4(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

class TestDictionary(unittest.TestCase):
    def test_dict(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        exp_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r1.to_dictionary(), exp_dict)

    def test_dict(self):
        r2 = Rectangle(5, 2, 6, 4, 5)
        exp_dict = {'id': 5, 'width': 5, 'height': 2, 'x': 6, 'y': 4}
        self.assertEqual(r2.to_dictionary(), exp_dict)

    def test_dict(self):
        r3 = Rectangle(1, 2, 3,)
        exp_dict = {'id': None, 'width': 1, 'height': 2, 'x': 3, 'y': 0}
        self.assertEqual(r3.to_dictionary(), exp_dict)

    def test_dict(self):
        r4 = Rectangle(1, 2,)
        exp_dict = {'id': 8, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(r4.to_dictionary(), exp_dict)

