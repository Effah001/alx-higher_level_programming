#!/usr/bin/python3
"""
The function returns True for object which is an instance
"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
