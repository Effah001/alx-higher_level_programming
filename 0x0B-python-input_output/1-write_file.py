#!/usr/bin/python3
"""documentation for write file"""


def write_file(filename="", text=""):
    """open a file, create if it doesn't exist"""
    with open(filename, 'w') as f:
        return f.write(text)
