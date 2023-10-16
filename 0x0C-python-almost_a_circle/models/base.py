#!/usr/bin/python3
"""
The script for our base class
"""


class Base:
    """ Create base class and assign a public
    instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the class"""
        if id is not None and not isinstance(id, int):
            raise ValueError("Id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
