#!/usr/bin/python3
"""
Documentation for 0-read_file
"""

def read_file(filename=""):
    """read the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
