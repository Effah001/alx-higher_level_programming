#!/usr/bin/python3
""" 
    A function that returns JSON
    representation
"""
import json


def to_json_string(my_obj):
    """Converts Python object to JSON string"""
    return json.dumps(my_obj)
