#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):

    def test_max_int(self):
        self.assertEqual(max_int([2, 4, 6, 8]), 8)
        self.assertEqual(max_int([1, -2]), 1)
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([-3, -2, -1]), -1)
        self.assertEqual(max_int([1]), 1)
        self.assertEqual(max_int([4, 4, 4]),4)
