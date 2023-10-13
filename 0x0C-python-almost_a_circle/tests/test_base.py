#!/usr/bin/python3
"""
Unittest for Base Class
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_unique_ids(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_same_ids(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)


    def test_increment_attributes(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj2.id, obj1.id +1)
        self.assertEqual(obj3.id, obj2.id +1)

    def test_assigned_id(self):
        with self.assertRaises(ValueError):
            obj = Base(id="id")
            obj = Base(id=0.67)

