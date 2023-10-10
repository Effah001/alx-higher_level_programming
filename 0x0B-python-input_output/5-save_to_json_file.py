#!/usr/bin/python3
"""Documentation of the 5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the JSON representation of an object to a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
