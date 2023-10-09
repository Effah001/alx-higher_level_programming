#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible
"""


def add_att(obj, att, value):
    """
    adds a new attribute to an objecif it’s possible
    """
    if not hasattr(att, "_dict_"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
