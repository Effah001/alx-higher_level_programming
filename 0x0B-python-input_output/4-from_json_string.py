#!/usr/bin/python3
""" A function that returns python
representation
"""
import json


def from_json_string(my_str):
    """Converts Python object to JSON string"""
    return json.loads(my_str)
