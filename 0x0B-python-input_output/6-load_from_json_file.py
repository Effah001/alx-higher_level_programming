#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
        Writes the JSON representation of 
        an object to a file
    """
    with open(filename, 'w') as f:
        return json.loads(f)
