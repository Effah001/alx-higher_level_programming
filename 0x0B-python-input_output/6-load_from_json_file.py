#!/usr/bin/python3
"""Documentation for load_from_json_fle"""
import json


def load_from_json_file(filename):
    """Writes the JSON representation of an object to a file"""
    with open(filename, 'r') as f:
        return json.load(f)
