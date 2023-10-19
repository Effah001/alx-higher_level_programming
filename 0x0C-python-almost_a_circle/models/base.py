#!/usr/bin/python3
"""
The script for our base class
"""
import json


class Base:
    """Create base class and assign a public
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionary to JSON string."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON stirng to a file"""
        file_name = cls.__name__ + ".json"
           j_list = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, "w", encoding="utf-8") as dt:
            dt.write(cls.to_json_string(j_list))
