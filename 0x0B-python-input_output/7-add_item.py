#!/usr/bin/python3
"""
Documentation for add_item
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"

if os.path.exist(file):
    data = load_from_json_file(file)
else:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, file)
