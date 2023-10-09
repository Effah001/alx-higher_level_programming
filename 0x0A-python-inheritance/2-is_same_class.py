#!/usr/bin/python3
"""
Documentation for ```2-is_same_class```
"""


def is_same_class(obj, a_class):
    """
    Compare two objects if they are the same
    """
    if type(obj) == a_class:
        return True
    return False
