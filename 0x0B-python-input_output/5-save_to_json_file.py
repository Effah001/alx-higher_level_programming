#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
        Writes the JSON representation of 
        an object to a file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

